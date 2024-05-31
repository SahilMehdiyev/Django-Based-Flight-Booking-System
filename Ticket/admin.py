from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('reservation',
                    'ticket_number',
                    'created_at',
                    'updated_at', )
    list_filter = ('reservation', )
    ordering = ('created_at', )
    search_fields = ('ticket_number', )
    
    

admin.site.register(Ticket,TicketAdmin)