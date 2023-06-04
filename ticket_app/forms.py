from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Ticket

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'cin')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'cin': forms.TextInput(attrs={'class': 'form-control', 'id': 'cin'}),
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'transport_type',
            'start_city',
            'destination_city',
            'comfort_level',
        ]
        widgets = {
            'transport_type': forms.Select(attrs={'class': 'form-control', 'name': 'transport_type', 'id': 'id_transport_type'}),
            'start_city': forms.Select(attrs={'class': 'form-control', 'name': 'start_city', 'id': 'id_start_city', 'placeholder': 'Start city'}),
            'destination_city': forms.Select(attrs={'class': 'form-control', 'name': 'destination_city', 'id': 'id_destination_city', 'placeholder': 'Destination city'}),
            'comfort_level': forms.Select(attrs={'class': 'form-control', 'name': 'comfort_level', 'id': 'id_comfort_level', 'placeholder': 'Comfort level'}),
        }