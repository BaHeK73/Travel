from django.db import models
from apps.common.models import City

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey('common.City', on_delete=models.CASCADE, related_name='hotels')
    address = models.CharField(max_length=700)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hotels', null=True, blank=True)
    stars = models.IntegerField(default=0)
    reviews_count = models.IntegerField(default=0)
    amenities = models.ManyToManyField('amenity', blank=True)


class Amenity(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='amenities')


class Room(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='rooms')
    room_type = models.ManyToManyField('RoomType', blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)
    capacity = models.IntegerField(default=2)
    is_available = models.BooleanField(default=True)


class RoomType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name