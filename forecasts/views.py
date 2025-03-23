from rest_framework import generics
from .models import Forecast
from .serializers import ForecastSerializer, ForecastByLocationSerializer
from .pagination import ForecastPagination, ForecastByLocationPagination

class ForecastListCreateView(generics.ListCreateAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    pagination_class = ForecastPagination

class ForecastRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

class ForecastByLocationListView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastByLocationSerializer
    pagination_class = ForecastByLocationPagination

    def get_queryset(self):
        return Forecast.objects.filter(location__id=self.kwargs['pk'])