from django.contrib import admin
from .models import Hotel, Amenity, Room, RoomType

admin.site.register(Hotel)
admin.site.register(Amenity)
admin.site.register(Room)
admin.site.register(RoomType)
