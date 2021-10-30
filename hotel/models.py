from typing import Optional
from django.db import models
from django import forms


ROOM_CHOICES =(
    ("1", "Standard single"),
    ("2", "Standard 2 beds"),
    ("3", "Standard king size bed"),
    ("4", "Premium single"),
    ("5", "Premium 2 beds"),
    ("6", "Premium king size bed"),
)

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, unique=True, blank=False)
    address = models.CharField(max_length=100, blank=False)
    postal_code = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=True)
    hotel_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return "Hotel No: "+ str(self.id) + " - " + str(self.hotel_name)

class Room(models.Model):

    ROOM_CHOICES =(
    ("1", "Standard single"),
    ("2", "Standard 2 beds"),
    ("3", "Standard king size bed"),
    ("4", "Premium single"),
    ("5", "Premium 2 beds"),
    ("6", "Premium king size bed"),
    )


    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField(blank=False)
    room_type = models.CharField(max_length = 30, choices=ROOM_CHOICES, default='1')
    availability = models.BooleanField(default=False)
    price_per_night = models.IntegerField(blank=False)
    description = models.CharField(max_length=500, blank=True)
    

    def __str__(self):
        return "Room No: "+ str(self.room_number) + " from hotel: " + str(self.hotel.hotel_name)



