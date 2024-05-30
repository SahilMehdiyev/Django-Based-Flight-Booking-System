from django.db import models


class Airline(models.Model):
    airline_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.airline_name
    