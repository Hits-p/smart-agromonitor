from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('agro_data')
client.switch_database('agro_data')
print("InfluxDB Database Created")
