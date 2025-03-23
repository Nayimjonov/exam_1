from django.urls import path
from . import views


urlpatterns = [
    path('analytics/temperature-avg/', views.temperature_avg_view, name='temperature_avg'),
    path('analytics/precipitation-sum/', views.precipitation_sum_view, name='precipitation_sum'),
    path('analytics/wind-speed-max/', views.max_wind_speed_view, name='max_wind_speed'),
]