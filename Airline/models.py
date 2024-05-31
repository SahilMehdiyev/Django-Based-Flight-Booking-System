from django.db import models


class Airline(models.Model):
    airline_name = models.TextField(max_length=100)
    
    
    
    class Meta:
        verbose_name = 'Airline'
        verbose_name_plural = 'Airlines'
    
    def __str__(self):
        return self.airline_name
    