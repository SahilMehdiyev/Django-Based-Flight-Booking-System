from django.urls import path
from .views import (
                   FlightListView,
                   FlightSearchView,
                   FlightCreateAPIView,
                   FlightDetailAPIView,
              
)

urlpatterns = [

    path('flight/create/', FlightCreateAPIView.as_view(), name='create'),
    path('flights/',FlightListView.as_view(),name='flights'),
    path('flight/search/',FlightSearchView.as_view(), name='search'),
    path('flights/<int:pk>/', FlightDetailAPIView.as_view(), name='flight_detail'),
]
