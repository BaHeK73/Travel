from django.db import models
from django.conf import settings
from Travel.apps.hotels.models import Hotel, Room
from Travel.apps.flights.models import Flight

class Booking(models.Model):
    BOOKING_TYPE = [
        ('hotel', 'Hotel'),
        ('flight', 'Flight'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    type = models.CharField(max_length=10, choices=BOOKING_TYPE)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.SET_NULL)
    flight = models.ForeignKey(Flight, null=True, blank=True, on_delete=models.SET_NULL)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    guests = models.IntegerField(default=1)
    status = models.CharField(max_length=20, default='pending')
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        if self.type == 'hotel':
            return f"Hotel Booking #{self.pk} — {self.hotel}"
        else:
            return f"Flight Booking #{self.pk} — {self.flight}"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    method = models.CharField(max_length=30)
    transaction_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
