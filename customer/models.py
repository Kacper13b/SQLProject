from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import *


class RoomReservation(models.Model):
    arrival_date = models.DateTimeField(blank=False)
    departure_date = models.DateTimeField(blank=False)
    number_of_adults = models.IntegerField(blank=False)
    number_of_children = models.IntegerField(blank=False)

    def __str__(self):
        return "Reservation no. " + str(self.id)


class Bill(models.Model):
    reservation = models.OneToOneField(RoomReservation, on_delete=models.CASCADE)
    total_room_price = models.FloatField(blank=False)
    restauration_bill = models.FloatField(blank=True)
    bar_bill = models.FloatField(blank=True)
    date_of_payment = models.DateTimeField(blank=False)
    credit_card_number = models.IntegerField(blank=False)
    payment_state = models.BooleanField(default=False)

    def __str__(self):
        return "Bill no. " + str(self.id)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', verbose_name='user')
    passport_number = models.CharField(max_length=100, null=True)
    telephone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    bill = models.ForeignKey(Bill, blank=True, null=True, on_delete=models.CASCADE)



    def __str__(self):
        return str(self.id) + ". " + self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """when user created create profile"""
    if created:
        Customer.objects.create(user=instance)


class AdditionalService(models.Model):
    SERVICE_CHOICES =(
    ("1", "Massage"),
    ("2", "SPA"),
    ("3", "Romantic Dinner"),
    ("4", "Swimming Pool"),
    ("5", "Trip"),
    ("6", "Breakfast in bed"),
    )


    service_type = models.CharField(max_length = 30, choices=SERVICE_CHOICES, default='1')
    price = models.FloatField(blank=True)
    additional_info = models.CharField(max_length = 500, blank=True)
    bill = models.ForeignKey(Bill, blank=False, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "Additional service no. " + str(self.id)

