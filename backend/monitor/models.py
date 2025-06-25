from django.db import models

class SensorReading(models.Model):
    device_id = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_id} @ {self.timestamp}"