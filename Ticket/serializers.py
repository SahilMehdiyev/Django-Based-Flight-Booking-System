
from .models import Ticket
from rest_framework import serializers

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['reservation', 'ticket_number','seat_number', 'created_at', 'updated_at']
        
        