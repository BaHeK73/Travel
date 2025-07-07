from django.contrib import admin
from .models import Amenity, Hotel, Room, HotelImage

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    search_fields = ['name']

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 0

class RoomInline(admin.TabularInline):
    model = Room
    extra = 0

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'stars', 'rating', 'reviews_count']
    list_filter = ['city', 'stars']
    search_fields = ['name', 'city__name']
    inlines = [RoomInline, HotelImageInline]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room_type', 'price_per_night', 'capacity', 'is_available']
    list_filter = ['hotel', 'room_type', 'is_available']
    search_fields = ['hotel__name', 'room_type']

@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'alt']
    list_filter = ['hotel'] 