
import requests
import random
import time

# Replace this with your actual API endpoint URL
API_URL = "http://127.0.0.1:8000/api/sensor-readings/"

def send_sensor_data():
    url = "http://127.0.0.1:8000/data/"
    device_id = "sensor-001"  # <-- moved inside the function
    while True:
        data = {
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(40.0, 60.0), 2),
            "device_id": device_id
        }
        try:
            response = requests.post(API_URL, json=data)
            print(f"Sent: {data} | Status: {response.status_code} | Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send data: {e}")
        
        time.sleep(5)  # Wait 5 seconds before sending next data

if __name__ == "__main__":
    send_sensor_data()