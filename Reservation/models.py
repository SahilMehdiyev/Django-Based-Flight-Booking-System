import sys
from django.db import models

sys.path.append('/home/sahil/Desktop/FlightApi')
from Flights.models import Flight
from users.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    passenger_phone = models.CharField(max_length=20)
    reservation_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation for {self.passenger_name} on {self.flight}"
    


