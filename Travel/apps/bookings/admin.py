from django.contrib import admin
from .models import Booking, Payment

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'hotel', 'room', 'flight', 'date_from', 'date_to', 'status', 'paid']
    list_filter = ['type', 'status', 'paid', 'hotel', 'flight']
    search_fields = ['user__username', 'hotel__name', 'flight__flight_number']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['booking', 'amount', 'status', 'method', 'created_at']
    list_filter = ['status', 'method']
    search_fields = ['booking__user__username', 'transaction_id']
