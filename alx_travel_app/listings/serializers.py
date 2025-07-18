"""
Serializers of listings application.

BookingSerializer:
    Processes and validates Booking model data.

ListingSerializer:
    Processes and validates Listing model data.

ReviewSerializer:
    Processes and validates Review model data.

UserSerializer:
    Processes and validates User model data.
"""

from alx_travel_app.listings.models import Booking, Listing, Review, User

from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    """Processes and validates Booking model data."""
    class Meta:
        model = Booking
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    """Processes and validates Listing model data."""
    class Meta:
        model = Listing
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Processes and validates Review model data."""
    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Processes and validates User model data."""
    class Meta:
        model = User
        fields = '__all__'