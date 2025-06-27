from django.db import models
from django.conf import settings

class HotelReviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hotel_reviews')
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)