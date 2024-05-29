from django.urls import path
from .views import TicketListAPIView

urlpatterns = [
    path('ticket/', TicketListAPIView.as_view(), name='ticket'),
   
]

