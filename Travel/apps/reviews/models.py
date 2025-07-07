from django.db import models
from django.conf import settings
from Travel.apps.hotels.models import Hotel
from Travel.apps.flights.models import Flight

class HotelReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hotel_reviews')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} on {self.hotel}"

class FlightReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='flight_reviews')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} on {self.flight}"
