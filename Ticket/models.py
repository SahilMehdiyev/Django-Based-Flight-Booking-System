import sys
from django.db import models



sys.path.append('/home/sahil/Desktop/FlightApi/')
from Reservation.models import Reservation

class Ticket(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE,related_name='tickets')
    ticket_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ticket_number


    
    
    