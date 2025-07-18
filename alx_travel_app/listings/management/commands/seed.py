from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from alx_travel_app.listings.models import User, Listing, Booking, Review

import random


class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        # Clear old data
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        get_user_model().objects.exclude(is_superuser=True).delete()

        # Create hosts
        hosts = []
        for i in range(3):
            host = get_user_model().objects.create_user(
                username=f'host{i}',
                email=f'host{i}@example.com',
                password='pass1234',
                role='HOST'
            )
            hosts.append(host)

        # Create guests
        guests = []
        for i in range(5):
            guest = get_user_model().objects.create_user(
                username=f'guest{i}',
                email=f'guest{i}@example.com',
                password='pass1234',
                role='GUEST'
            )
            guests.append(guest)

        # Create listings
        listings = []
        types = ['APARTMENT', 'ROOM', 'TOUR', 'CAR']
        for i in range(10):
            listing = Listing.objects.create(
                title=f'Listing {i}',
                description='A nice place to stay.',
                location='City '+ str(i),
                price=random.randint(50, 300),
                type=random.choice(types),
                host=random.choice(hosts),
            )
            listings.append(listing)

        # Create bookings
        for i in range(8):
            check_in = timezone.now().date()
            check_out = check_in + timezone.timedelta(days=random.randint(1, 10))
            Booking.objects.create(
                listing=random.choice(listings),
                guest=random.choice(guests),
                check_in=check_in,
                check_out=check_out,
                total_price=random.randint(100, 1000),
                status=random.choice(['PENDING', 'CONFIRMED']),
            )

        # Create reviews
        for i in range(10):
            Review.objects.create(
                listing=random.choice(listings),
                guest=random.choice(guests),
                rating=random.randint(1, 5),
                comment='Great experience!',
            )

        self.stdout.write(self.style.SUCCESS("✅ Seeding complete!"))
