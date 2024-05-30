from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('users.urls')),
    path('api/',include('Payment.urls')),
    path('api/',include('Reservation.urls')),
    path('api/',include('Ticket.urls')),
    path('api/',include('Airline.urls')),
    path('api/',include('Flights.urls')),
]
