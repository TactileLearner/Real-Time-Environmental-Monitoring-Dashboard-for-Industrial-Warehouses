
import requests, time, random

while True:
    data = {
        "device_id": "sim_001",
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 70), 2),
    }
    try:
        requests.post("http://127.0.0.1:8000/api/data/", json=data)
    except:
        print("Server not responding")
    time.sleep(2)