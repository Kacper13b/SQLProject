import json
from django.contrib import admin
from .models import Hotel, Room, Bar, Restaurant, Team, Employee
import decimal
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models import Sum


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
    list_display = ('id', 'hotel', 'department')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','salary', 'team')
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

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Employee.objects.values('team')
            .order_by('team')
            .annotate(y=Sum('salary'))
        )

        print(Employee.objects.values('team').order_by('team').annotate(total_price=Sum('salary')))
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    update_status_raise.short_description = "Raise salary by 10 percent"
    update_status_decrease.short_description = "Decrease salary by 10 percent"

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Bar,BarAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Employee,EmployeeAdmin)

