from django.urls import path
from .views import AirlineListView

urlpatterns = [
    path('airlines/',AirlineListView.as_view(),name='airlines'),
]
