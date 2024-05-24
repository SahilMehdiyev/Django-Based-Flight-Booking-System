from django.urls import path
from .views import LoginView,FlighListView,FlightSearchView


urlpatterns = [

    path('login/',LoginView.as_view(),name='login'),
    path('flight/',FlighListView.as_view(),name='flight'),
    path('search/',FlightSearchView.as_view(), name='search'),

]
