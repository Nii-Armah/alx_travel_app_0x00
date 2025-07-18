"""
Serializers of listings application.

ListingSerializer:
    Processes and validates Listing model data.

UserSerializer:
    Processes and validates User model data.
"""

from alx_travel_app.listings.models import Listing, User

from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    """Processes and validates Listing model data."""
    class Meta:
        model = Listing
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Processes and validates User model data."""
    class Meta:
        model = User
        fields = '__all__'