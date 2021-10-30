from django.contrib import admin
from .models import Hotel, Room

class HotelAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Room,RoomAdmin)
