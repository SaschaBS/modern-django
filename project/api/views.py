from django.shortcuts import render

# Create your views here.

from project.api.models import Country, Airport, Flight
from rest_framework import viewsets
from project.api.serializers import CountrySerializer, AirportSerializer, FlightSerializer

class AirportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class FlightViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
