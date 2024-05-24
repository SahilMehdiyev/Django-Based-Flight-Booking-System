from django.urls import path
from .views import (LoginView,
                   FlighListView,
                   FlightSearchView,
                   FlightCreateAPIView,
                   FlightDetailAPIView)

urlpatterns = [

    path('login/',LoginView.as_view(),name='login'),
    path('flight/create/', FlightCreateAPIView.as_view(), name='create'),
    path('flights/',FlighListView.as_view(),name='flights'),
    path('search/',FlightSearchView.as_view(), name='search'),
    path('flights/<int:pk>/', FlightDetailAPIView.as_view(), name='flight_detail'),
    # path('flights/<int:pk>/', FlightRetrieveUpdateDestroyAPIView.as_view(), name='flight_rud'),

]
