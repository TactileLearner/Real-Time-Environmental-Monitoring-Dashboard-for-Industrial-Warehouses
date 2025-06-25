
# monitor/tasks.py

from celery import shared_task

@shared_task
def send_alert_email(sensor_id, temperature, humidity):
    # Simulated alert (no-op)
    print(f"Alert: Sensor {sensor_id}, Temp: {temperature}, Humidity: {humidity}")