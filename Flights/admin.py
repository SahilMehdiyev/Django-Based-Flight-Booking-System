from django.contrib import admin
from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    list_display = ('departure_city','arrivel_city','departure_date','arrivel_date','airline','price')
    list_filter = ('departure_city',)
    search_fields = ('departure_city',)
    ordering = ('departure_date',)
    

admin.site.register(Flight,FlightAdmin)