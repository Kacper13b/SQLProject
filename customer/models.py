from django.db import models
from hotel.models import Hotel, Room, Employee, Team

class Customer(models.Model):
    passport_number = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    telephone_number = models.IntegerField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    postal_code = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    room = models.ForeignKey(Room, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ". " + str(self.first_name) + " " + str(self.last_name)

