from django.contrib import admin
from .models import HotelReview, FlightReview

@admin.register(HotelReview)
class HotelReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'hotel', 'rating', 'created_at']
    list_filter = ['hotel', 'rating']
    search_fields = ['user__username', 'hotel__name']

@admin.register(FlightReview)
class FlightReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'flight', 'rating', 'created_at']
    list_filter = ['flight', 'rating']
    search_fields = ['user__username', 'flight__flight_number']
