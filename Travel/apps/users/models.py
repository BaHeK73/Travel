from django.contrib.auth.models import AbstractUser
from django.db import models

from Travel.apps.flights.models import Flight
from Travel.apps.hotels.models import Hotel


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    favourites_hotels = models.ManyToManyField(Hotel, blank=True, related_name='favourited_by')
    favourites_flights = models.ManyToManyField(Flight, blank=True, related_name='favourited_by')
