from flask import Flask, request, jsonify
import psycopg2
from influxdb import InfluxDBClient
from flask import Flask, jsonify, render_template, redirect, url_for
import io, base64
import matplotlib.pyplot as plt
from flask import Response
app = Flask(__name__)

# PostgreSQL connection
pg_conn = psycopg2.connect(
    dbname="agro_db", user="postgres", password="postgres", host="localhost", port="5432"
)
pg_cursor = pg_conn.cursor()

# InfluxDB connection
influx_client = InfluxDBClient(host='localhost', port=8086)
influx_client.switch_database('agro_data')

@app.route('/')
def index():
    # Option A – serve a dashboard page
    return render_template('index.html')

    # Option B – if you’d rather redirect to another route
    # return redirect(url_for('dashboard'))


@app.route('/data', methods=['POST'])
def collect_data():
    data = request.json

    # Insert into PostgreSQL
    pg_cursor.execute("""
        INSERT INTO sensor_data (temperature, humidity, soil_moisture, ph, light)
        VALUES (%s, %s, %s, %s, %s)

    """, (data['temperature'], data['humidity'], data['soil_moisture'], data['ph'], data['light']))
    pg_conn.commit()

    # Insert into InfluxDB
    influx_data = [{
        "measurement": "environment",
        "fields": {
            "temperature": data['temperature'],
            "humidity": data['humidity'],
            "soil_moisture": data['soil_moisture'],
            "ph": data['ph'],
            "light": data['light']
        }
    }]
    influx_client.write_points(influx_data)

    return jsonify({"status": "success"}), 200
@app.route('/plot.png')
def plot_png():
    # 1️⃣ Calculate / query your numbers
    labels  = ['A', 'B', 'C', 'D']
    values  = [12, 19, 3, 5]

    # 2️⃣ Draw with matplotlib (no GUI)
    plt.clf()
    plt.bar(labels, values)

    # 3️⃣ Stream as PNG
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return Response(buf.getvalue(), mimetype='image/png')
if __name__ == '__main__':
    app.run(debug=True)
    
    
@app.route('/plot.png')
def plot_png():
    # 1️⃣ Get or compute the values you want to plot
    labels = ['A', 'B', 'C', 'D']         # ← dummy data; replace with live sensor data
    values = [12, 19, 3, 5]

    # 2️⃣ Draw the bar‑chart in memory (no GUI window)
    plt.clf()                             # clear any previous figure
    plt.bar(labels, values)

    # 3️⃣ Stream the figure back as a PNG
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return Response(buf.getvalue(), mimetype='image/png')   

@app.route('/data', methods=['POST'])
def collect_data():
    data = request.json
    try:
        # PostgreSQL insert
        pg_cursor.execute(
            "INSERT INTO sensor_data (temperature, humidity, soil_moisture, ph, light) "
            "VALUES (%s, %s, %s, %s, %s)",
            (data['temperature'], data['humidity'], data['soil_moisture'],
             data['ph'], data['light'])
        )
        pg_conn.commit()
        print("✅  Inserted into Postgres:", data)     # <= NEW
    except Exception as e:
        pg_conn.rollback()
        print("❌ Postgres error:", e)

    # Influx insert (unchanged) ...
    return jsonify({"status": "success"}), 200
