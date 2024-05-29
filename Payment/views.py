
from rest_framework.response import Response
from .models import Payment
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework.generics import CreateAPIView
from .serializers import PaymentSerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import ValidationError
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY            

class PaymentListView(APIView):
    def get(self,request, *args, **kwargs):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
     


# class OrderCreateView(APIView):
#     def post(self,request, *args, **kwargs):
#         serializer = OrderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         #stripe uzerinden odeme islemini baslat
#         token = request.data.get('token')
#         amount = request.data.get('amount')
#         charge = stripe.Charge.create(
#             amount = int(amount*100),
#             currency='try',
#             source=token,
#         )
        
#         #Order ve Payment modellerini kaydet
        
#         order = serializer.save(user=request.user)
#         Payment.objects.create(order=order, stripe_charge_id=charge.id,amount=amount)
        
#         return Response(serializer.data, status=201)
    

