from django.contrib import admin
from .models import Customer, RoomReservation, Bill, AdditionalService

# Register your models here




class RoomReservationAdmin(admin.ModelAdmin):
    pass

class BillAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass

class AdditionalServiceAdmin(admin.ModelAdmin):
    pass





admin.site.register(RoomReservation,RoomReservationAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(AdditionalService,AdditionalServiceAdmin)