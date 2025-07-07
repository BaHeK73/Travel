from django.contrib import admin
from .models import City, Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['country']
    search_fields = ['name', 'country__name']
