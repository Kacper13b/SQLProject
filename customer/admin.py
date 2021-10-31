from django.contrib import admin
from .models import Customer, RoomReservation

# Register your models here



class CustomerAdmin(admin.ModelAdmin):
    pass

class RoomReservationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer,CustomerAdmin)



admin.site.register(RoomReservation,RoomReservationAdmin)
