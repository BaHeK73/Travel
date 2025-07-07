from django.db import models
from Travel.apps.common.models import City

class Airport(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Airline(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='airlines/', null=True, blank=True)

    def __str__(self):
        return self.name

class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='flights')
    flight_number = models.CharField(max_length=50)
    departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    seats_available = models.IntegerField(default=0)
    baggage_included = models.BooleanField(default=True)
    is_direct = models.BooleanField(default=True)
    cabin_class = models.CharField(max_length=50, default='Economy')

    def __str__(self):
        return f"{self.flight_number}: {self.departure_airport} → {self.arrival_airport}"
