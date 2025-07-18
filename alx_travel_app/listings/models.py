"""
Data models for listings application.

User:
    A user of the system.

Listing:
    A bookable travel-related item or service.

Booking:
    A guest reservation for a listing.

Review:
    A guest feedback about a listing.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid


class User(AbstractUser):
    """A user of the system."""
    class Meta:
        db_table = 'users'

    class Role(models.TextChoices):
        """Roles of users."""
        HOST = 'HOST', 'Host'
        GUEST = 'GUEST', 'Guest'


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique identification of user'
    )

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.GUEST,
        help_text='Type of user'
    )

    def __str__(self) -> str:
        return self.username


class Listing(models.Model):
    """A bookable travel-related item or service."""
    class Meta:
        db_table = 'listings'

    class Type(models.TextChoices):
        """Types of listings."""
        APARTMENT = 'APARTMENT', 'Apartment'
        ROOM = 'ROOM', 'Room'
        TOUR = 'TOUR', 'Tour'
        CAR = 'CAR', 'Car'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique identification of listing'
    )

    title = models.CharField(max_length=100, help_text='Title or name of listing')
    description = models.TextField(help_text='Description of listing')
    location = models.CharField(max_length=100, help_text='Location of listing')
    price = models.DecimalField(decimal_places=2, max_digits=10, help_text='Price of listing')
    type = models.CharField(max_length=20, choices=Type.choices, help_text='Type of listing')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Date and time of listing creation')
    updated_at = models.DateTimeField(auto_now=True, help_text='Date and time of last update of listing')
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings', help_text='Host of listing')

    def __str__(self) -> str:
        return self.title


class Booking(models.Model):
    """A guest reservation for a listing."""
    class Meta:
        db_table = 'bookings'

    class Status(models.TextChoices):
        """Status of guest reservations."""
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique identification of booking'
    )

    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='bookings',
        help_text='Listing that has been booked'
    )

    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings',
        help_text='Guest that is booked the listing'
    )

    total_price = models.DecimalField(decimal_places=2, max_digits=10, help_text='Total price of listing')
    check_in = models.DateField(help_text='Check in date of guest')
    check_out = models.DateField(help_text='Check out date of guest')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Date and time of booking creation')
    updated_at = models.DateTimeField(auto_now=True, help_text='Date and time of last update of booking')

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        help_text='Status of booking'
    )


class Review(models.Model):
    """A guest feedback about a listing."""
    class Meta:
        db_table = 'reviews'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique identification of review'
    )

    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Listing being reviewed'
    )

    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Guest giving review'
    )

    rating = models.IntegerField(help_text='Rating of review between 1 and 5')
    comment = models.TextField(blank=True, help_text='Review comment')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Date and time of review creation')
