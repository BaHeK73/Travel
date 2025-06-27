from django.db import models
from apps.common.models import City

class Airoport(models.Model):
    name = models.CharField(max_length=400)
    code = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airoports')