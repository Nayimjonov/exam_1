from django.contrib import admin
from .models import WeatherData


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'temperature', 'recorded_at')
    search_fields = ('name', 'temperature')
    list_filter = ('location',)