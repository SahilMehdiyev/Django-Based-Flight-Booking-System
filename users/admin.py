from django.contrib import admin
from .models import User,Flight,Airline

admin.site.register(User)
admin.site.register(Airline)
admin.site.register(Flight)
# admin.site.register(FlightFare)





