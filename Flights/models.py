import sys
from django.db import models


sys.path.append('/home/sahil/Desktop/FlightApi')
from Airline.models import Airline


class Flight(models.Model):
    
    departure_city = models.CharField(max_length=100)
    arrivel_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    arrivel_date = models.DateField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.airline} Flight from {self.departure_city} to {self.arrivel_city} on {self.departure_date}'
