from django.contrib import admin
from .models import Hotel, Room, Bar, Restaurant, Team, Employee
import decimal

class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel_name', 'stars','country')
    list_filter = ('id', 'hotel_name', 'stars','country')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type','availability', 'price_per_night')
    list_filter = ('room_number', 'room_type','availability', 'price_per_night')

class BarAdmin(admin.ModelAdmin):
    pass

class RestaurantAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(admin.ModelAdmin):
    actions = ['update_status_raise', 'update_status_decrease']

    def update_status_raise(self, request, queryset):
        obj = queryset.all()
        print(obj)
        for i in obj:
            i.salary *= decimal.Decimal(1.1)
            i.save()

    def update_status_decrease(self, request, queryset):
        obj = queryset.all()
        print(obj)
        for i in obj:
            i.salary *= decimal.Decimal(0.9)
            i.save()

    update_status_raise.short_description = "Raise salary by 10 percent"
    update_status_decrease.short_description = "Decrease salary by 10 percent"

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Bar,BarAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Employee,EmployeeAdmin)

