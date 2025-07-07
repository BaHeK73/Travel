from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    img_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.country.code}"
