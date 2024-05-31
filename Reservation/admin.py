from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
                    'user',
                    'flight',
                    'passenger_name',
                    'passenger_email',
                    'passenger_phone',
                    'reservation_date',
                    'total_price',
                    'is_paid',)
    list_filter = ('reservation_date',)
    search_fields = ('passenger_name',)


admin.site.register(Reservation,ReservationAdmin)
