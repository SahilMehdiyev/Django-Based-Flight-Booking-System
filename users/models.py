from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,PermissionsMixin,BaseUserManager
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
    
    


class Flight(models.Model):
    departue_city = models.CharField(max_length=100)
    arrivel_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    arrivel_date = models.DateField()
    airline = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return f'{self.airline} Flight from {self.departue_city} to {self.arrivel_city} on {self.departure_date}'