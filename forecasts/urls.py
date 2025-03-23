from django.urls import path
from . import views


urlpatterns = [
    path('forecasts/', views.ForecastListCreateView.as_view(), name='list_create'),
    path('forecasts/<int:pk>/', views.ForecastRetrieveUpdateDestroyView.as_view(), name='detail'),
    path('forecasts/location/<int:pk>/', views.ForecastByLocationListView.as_view(), name='forecast_by_location_list'),
]
