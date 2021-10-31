from typing import Optional
from django.db import models
from django import forms
from customer.models import Customer, RoomReservation


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
    stars = models.IntegerField(blank=False)
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
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    reservation = models.ForeignKey(RoomReservation, blank=True, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return "Room No: "+ str(self.room_number) + " from hotel: " + str(self.hotel.hotel_name)


class Bar(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField(blank=False)
    number_of_employees = models.IntegerField(blank=False)

    def __str__(self):
        return "Bar No: "+ str(self.id) + " from hotel: " + str(self.hotel.hotel_name)


class Restaurant(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number_of_tables = models.IntegerField(blank=False)
    number_of_seats = models.IntegerField(blank=False)
    stars = models.IntegerField(blank=False)
    kitchen_type = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.kitchen_type) + " Restaurant No: "+ str(self.id) + " from hotel: " + str(self.hotel.hotel_name)


class Team(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True)
    number_of_employees = models.IntegerField(blank=False)

    def __str__(self):
        return "Working team no: "+ str(self.id) + " from hotel - " + str(self.hotel.hotel_name)


class Employee(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    salary = models.FloatField(blank=False)
    date_of_employment = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return "Employee no: "+ str(self.id) + " - " + str(self.first_name) + " " + str(self.last_name)
    
