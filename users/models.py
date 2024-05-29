# from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
import uuid
        
class User(AbstractUser):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(('email address'))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    
    
    
class Airline(models.Model):
    airline_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.airline_name
    


class Flight(models.Model):
    
    departue_city = models.CharField(max_length=100)
    arrivel_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    arrivel_date = models.DateField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.airline} Flight from {self.departue_city} to {self.arrivel_city} on {self.departure_date}'



# class FlightFare(models.Model):
#     flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
#     # departure_date = models.DateField()
#     # departure_time = models.TimeField()
#     # arrival_date = models.DateField()
#     # arrival_time = models.TimeField()
#     # origin_airport = models.CharField(max_length=100)
#     # destination_airport = models.CharField(max_length=100)
#     # airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
#     seat_class = models.CharField(max_length=50)
#     base_fare = models.DecimalField(max_digits=10, decimal_places=2)
#     taxes_and_fees = models.DecimalField(max_digits=10, decimal_places=2)
#     total_fare = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



