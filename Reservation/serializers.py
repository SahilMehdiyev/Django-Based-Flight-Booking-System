from .models import Reservation
from rest_framework import serializers



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['user', 'flight', 'passenger_name', 'passenger_email', 'passenger_phone', 'reservation_date', 'total_price', 'is_paid']

