"""
Data models for listings application.

User:
    A user of the system.
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
        help_text='Type of user'
    )
