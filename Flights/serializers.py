from .models import Flight
from rest_framework import serializers

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'departure_city', 'arrivel_city', 'departure_date', 'arrivel_date', 'airline', 'price']
