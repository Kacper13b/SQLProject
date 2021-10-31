from django.db import models

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

    def __str__(self):
        return str(self.id) + ". " + str(self.first_name) + " " + str(self.last_name)


class RoomReservation(models.Model):
    arrival_date = models.DateTimeField(blank=False)
    departure_date = models.DateTimeField(blank=False)
    number_of_adults = models.IntegerField(blank=False)
    number_of_children = models.IntegerField(blank=False)

    def __str__(self):
        return "Reservation no. " + str(self.id)




