from django.db import models
from Travel.apps.common.models import City

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='amenities/', null=True, blank=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    address = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)
    stars = models.IntegerField(default=0)
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='hotels')
    rating = models.FloatField(default=0)
    reviews_count = models.IntegerField(default=0)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f"{self.name} ({self.city})"

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=100, default='Standard')
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)
    capacity = models.IntegerField(default=2)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.hotel.name} — {self.room_type}"

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotel_gallery/')
    alt = models.CharField(max_length=255, blank=True)
