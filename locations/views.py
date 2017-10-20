from rest_framework import generics
from . import models
from . import serializers


class CityList(generics.ListAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class StateList(generics.ListAPIView):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class CountryList(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
