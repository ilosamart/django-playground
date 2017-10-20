from rest_framework import generics
from . import models
from . import serializers
import logging


class CityList(generics.ListAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class StateList(generics.ListAPIView):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class CountryList(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountryByCityPIBList(generics.ListAPIView):
    serializer_class = serializers.CountrySerializer

    def get_queryset(self):
        return models.Country.objects.filter(states__cities__pib__gt=self.kwargs['pib']).distinct()