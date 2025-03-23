from rest_framework import serializers
from .models import WeatherData


class WeatherLocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

class WeatherDataByLocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    temperature = serializers.FloatField(read_only=True)
    humidity = serializers.FloatField(read_only=True)
    pressure = serializers.FloatField(read_only=True)
    wind_speed = serializers.FloatField(read_only=True)
    wind_direction = serializers.FloatField(read_only=True)
    precipitation = serializers.FloatField(read_only=True)
    recorded_at = serializers.DateTimeField(read_only=True)

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = (
            'id',
            'location',
            'temperature',
            'humidity',
            'pressure',
            'wind_speed',
            'wind_direction',
            'precipitation',
            'recorded_at'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['location'] = WeatherLocationSerializer(instance.location).data
        return data