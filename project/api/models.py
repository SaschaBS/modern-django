from django.db import models
from django.utils.dateformat import format

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Airport(models.Model):
    iata_code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        'Country',
        related_name='airports',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Flight(models.Model):
    departure_airport = models.ForeignKey('Airport', related_name='departure_airport', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey('Airport', related_name='arrival_airport', on_delete=models.CASCADE)
    flight_date = models.DateField()

    def __str__(self):
        return self.departure_airport.iata_code + '->' + self.arrival_airport.iata_code 
