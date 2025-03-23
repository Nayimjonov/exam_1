from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer, WeatherDataByLocationSerializer
from .pagination import WeatherDataPagination, WeatherDataByLocationPagination

class WeatherDataListCreateView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    pagination_class = WeatherDataPagination


class WeatherDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


class WeatherDataByLocationListView(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataByLocationSerializer
    pagination_class = WeatherDataByLocationPagination

    def get_queryset(self):
        return WeatherData.objects.filter(location__id=self.kwargs['pk'])