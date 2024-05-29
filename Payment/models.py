import sys
from django.db import models
# from ..users.models import User,Reservation

sys.path.append('/home/sahil/Desktop/FlightApi')
from users.models import User
from Reservation.models import Reservation


class Payment(models.Model):
    """
    Model for handling payment transactions.
    """
    PAYMENT_METHODS = (
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    )

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    stripe_charge_id = models.CharField(max_length=50, null=True, blank=True)
    paypal_transaction_id = models.CharField(max_length=50, null=True, blank=True)
    bank_transaction_id = models.CharField(max_length=50, null=True, blank=True)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for Reservation {self.reservation.id}"
