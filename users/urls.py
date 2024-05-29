from django.urls import path
from .views import (
                   LoginView,
                   FlightListView,
                   FlightSearchView,
                   FlightCreateAPIView,
                   FlightDetailAPIView,
                #  FlightFareAPIView
                   ReservationListAPIView,
                   ReservationDetailAPIView,
                #  OrderCreateView,
)

urlpatterns = [

    path('login/',LoginView.as_view(),name='login'),
    path('flight/create/', FlightCreateAPIView.as_view(), name='create'),
    path('flights/',FlightListView.as_view(),name='flights'),
    # path('flightfare/<str:flight_id>/', FlightFareAPIView.as_view(), name='flight_fare'),
    path('flight/search/',FlightSearchView.as_view(), name='search'),
    path('flights/<int:pk>/', FlightDetailAPIView.as_view(), name='flight_detail'),
    # path('flights/<int:pk>/', FlightRetrieveUpdateDestroyAPIView.as_view(), name='flight_rud'),
    
    path('reservations/',ReservationListAPIView.as_view(), name='reservation_list'),
    path('reservations/<int:pk>/',ReservationDetailAPIView.as_view(), name='reservation-detail'),
    
    
    # path('orders/',OrderCreateView.as_view(), name='order'),

]
