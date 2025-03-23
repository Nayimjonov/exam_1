from django.db.models import Avg, Sum, Max
from rest_framework.decorators import api_view
from rest_framework.response import Response
from weatherdata.models import WeatherData



@api_view(['GET'])
def temperature_avg_view(request):
    avg_value = WeatherData.objects.aggregate(
        average_temperature=Avg('temperature')
    )
    return Response(avg_value)

@api_view(['GET'])
def precipitation_sum_view(request):
    sum_value = WeatherData.objects.aggregate(
        total_precipitation=Sum('precipitation')
    )
    return Response(sum_value)

@api_view(['GET'])
def max_wind_speed_view(request):
    max_value = WeatherData.objects.aggregate(
        max_wind_speed=Max('wind_speed')
    )
    return Response(max_value)

