"""
Data models for listings application.

User:
    A user of the system.

Listing:
    A bookable travel-related item or service.
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
        GUEST = 'GUEST', 'GUEST'


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


class Listing(models.Model):
    """A bookable travel-related item or service."""
    class Meta:
        db_table = 'listings'

    class Type(models.TextChoices):
        """Types of listings."""
        APARTMENT = 'APARTMENT', 'Apartment'
        ROOM = 'ROOM', 'Room'
        TOUR = 'TOUR', 'Tour'
        Car = 'CAR', 'Car'

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

    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='listings',
        help_text='Host of listing'
    )
