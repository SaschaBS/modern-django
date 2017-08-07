from project.api.models import Country, Airport, Flight
from rest_framework import serializers, relations

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    airports = serializers.HyperlinkedRelatedField(many=True, view_name = 'airport-detail', read_only='True')
    class Meta:
        model = Country
        fields = ('__all__')

class AirportSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.HyperlinkedRelatedField(view_name='country-detail',read_only='True')
    class Meta:
        model = Airport
        fields = ('iata_code', 'name', 'country')
        
class FlightSerializer(serializers.HyperlinkedModelSerializer):
    departure_airport = serializers.HyperlinkedRelatedField(many=False, view_name = 'airport-detail', read_only='True')
    arrival_airport = serializers.HyperlinkedRelatedField(many=False, view_name = 'airport-detail', read_only='True')
    class Meta:
        model = Flight
        fields = ('flight_date', 'departure_airport', 'arrival_airport')
