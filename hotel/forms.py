from .models import *
from django import forms
from customer.models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):

    arrival_date = forms.DateField(widget=DateInput(format="%d/%m/%Y"))
    departure_date = forms.DateField(widget=DateInput(format="%d/%m/%Y"))

    class Meta:
        model = RoomReservation
        fields = ('arrival_date', 'departure_date', 'number_of_adults', 'number_of_children')

        widgets = {
            'number_of_adults': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_children': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name','last_name','email','telephone_number','passport_number','address','city','postal_code','country')

        widgets = {
            
        }