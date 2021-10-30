from django.contrib import admin
from .models import Hotel, Room, Bar, Restaurant, Team, Employee

class HotelAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

class BarAdmin(admin.ModelAdmin):
    pass

class RestaurantAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Bar,BarAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Employee,EmployeeAdmin)

