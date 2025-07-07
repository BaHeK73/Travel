from django.contrib import admin
from .models import *

for model in [Airline, Airport, Flight]:
    admin.site.register(model)
