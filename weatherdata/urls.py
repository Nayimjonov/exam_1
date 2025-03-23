from django.urls import path
from . import views


urlpatterns = [
    path('weather-data/', views.WeatherDataListCreateView.as_view(), name='list_create'),
    path('weather-data/<int:pk>/', views.WeatherDataRetrieveUpdateDestroyView.as_view(), name='detail'),
    path('weather-data/location/<int:pk>/', views.WeatherDataByLocationListView.as_view(), name='weather_data_by_location_list'),
]
