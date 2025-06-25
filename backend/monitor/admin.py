from django.contrib import admin
from .models import SensorReading


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'temperature', 'humidity', 'timestamp')
    list_filter = ('device_id', 'timestamp')
    search_fields = ('device_id',)
    ordering = ('-timestamp',)