from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Ticket(models.Model):
    TRANSPORT_TYPE_CHOICES = (
        ('train', 'Train'),
        ('autocar', 'Autocar'),
    )
    START_CITY_CHOICES = (
        ('casablanca', 'Casablanca'),
        ('marrakech', 'Marrakech'),
        ('fes', 'Fes'),
        ('tangier', 'Tangier'),
    )
    COMFORT_LEVEL_CHOICES = (
        (1, '1st Class'),
        (2, '2nd Class'),
        (3, '3rd Class'),
    )
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_TYPE_CHOICES, verbose_name="Transport Type")
    start_time = models.DateTimeField(default=timezone.now, verbose_name="Start Time")
    start_city = models.CharField(max_length=12, choices=START_CITY_CHOICES, verbose_name="Start City")
    destination_city = models.CharField(max_length=12, choices=START_CITY_CHOICES, verbose_name="Destination City")
    arrival_time = models.DateTimeField(verbose_name="Arrival Time")
    comfort_level = models.PositiveSmallIntegerField(choices=COMFORT_LEVEL_CHOICES, verbose_name="Comfort Level")

    def save(self, *args, **kwargs):
        self.arrival_time = self.start_time + timedelta(hours=2)
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.start_city} to {self.destination_city} ({self.transport_type})"
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, cin, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, cin=cin, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, cin, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, first_name, last_name, cin, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cin = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cin']

    def __str__(self):
        return self.email
