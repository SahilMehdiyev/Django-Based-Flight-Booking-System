from django.contrib import admin
from .models import Airline


class AirlineAdmin(admin.ModelAdmin):
    list_display = ('airline_name', )
    list_filter = ('airline_name', )
    search_fields = ('airline_name', )
    
   
    

admin.site.register(Airline,AirlineAdmin)


