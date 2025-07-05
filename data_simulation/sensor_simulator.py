import requests
import random
import time

URL = "http://localhost:5000/data"

while True:
    data = {
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 90), 2),
        "soil_moisture": round(random.uniform(200, 800), 2),
        "ph": round(random.uniform(5.5, 7.5), 2),
        "light": round(random.uniform(100, 1000), 2)
    }
    response = requests.post(URL, json=data)
    print("Sent:", data, "Status:", response.status_code)
    time.sleep(5)