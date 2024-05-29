from .models import Payment
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        # fields = ['reservation', 'user', 'payment_method', 'is_successful']
        fields = '__all__'


