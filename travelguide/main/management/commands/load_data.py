from django.core.management.base import BaseCommand
from main.models import Destination, SliderImage, Hotel, Tag, Amenity

class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **kwargs):
        # Create destinations
        destinations = [
            {
                'name': 'Goa Beaches',
                'description': 'Explore the beautiful beaches of Goa with golden sands and clear blue waters. Perfect for relaxation and water sports.',
                'price': 15000,
                'duration': '5 Days / 4 Nights'
            },
            {
                'name': 'Kerala Backwaters',
                'description': 'Experience the serene backwaters of Kerala in traditional houseboats. Enjoy the lush green landscapes and local cuisine.',
                'price': 20000,
                'duration': '7 Days / 6 Nights'
            },
            {
                'name': 'Rajasthan Heritage',
                'description': 'Discover the royal heritage of Rajasthan with its magnificent forts, palaces, and vibrant culture.',
                'price': 25000,
                'duration': '8 Days / 7 Nights'
            },
            {
                'name': 'Himalayan Trek',
                'description': 'Adventure trek in the mighty Himalayas with breathtaking views and challenging trails for trekking enthusiasts.',
                'price': 18000,
                'duration': '6 Days / 5 Nights'
            },
            {
                'name': 'Andaman Islands',
                'description': 'Explore the pristine islands of Andaman with coral reefs, water sports, and exotic marine life.',
                'price': 30000,
                'duration': '7 Days / 6 Nights'
            },
            {
                'name': 'Varanasi Spiritual',
                'description': 'Experience the spiritual essence of Varanasi with Ganga Aarti, ancient temples, and sacred ghats.',
                'price': 12000,
                'duration': '4 Days / 3 Nights'
            }
        ]

        # slider images
        slider_images = [
            {
                'title': 'Discover Incredible India',
                'description': 'Explore the diverse landscapes, rich culture, and heritage of India with our expert guides.'
            },
            {
                'title': 'Best Tour Packages',
                'description': 'We offer the best customized tour packages at affordable prices.'
            },
            {
                'title': 'Luxury Travel Experience',
                'description': 'Enjoy luxury accommodations and personalized services on all our tours.'
            }
        ]

        self.stdout.write(self.style.SUCCESS('Creating sample data...'))
        
        # destinations 
        for dest in destinations:
            Destination.objects.create(**dest)
        
        # slider images
        for slide in slider_images:
            SliderImage.objects.create(**slide)
            
        self.stdout.write(self.style.SUCCESS('Successfully created sample data!'))


        # tags
        beach_tag = Tag.objects.create(name='beach')
        luxury_tag = Tag.objects.create(name='luxury')
        adventure_tag = Tag.objects.create(name='adventure')
        family_tag = Tag.objects.create(name='family')
        honeymoon_tag = Tag.objects.create(name='honeymoon')
        
        # amenities
        wifi = Amenity.objects.create(name='Free WiFi', icon='fa-wifi')
        pool = Amenity.objects.create(name='Swimming Pool', icon='fa-swimming-pool')
        spa = Amenity.objects.create(name='Spa', icon='fa-spa')
        restaurant = Amenity.objects.create(name='Restaurant', icon='fa-utensils')
        ac = Amenity.objects.create(name='Air Conditioning', icon='fa-snowflake')
        
        # destinations
        goa = Destination.objects.create(
            name='Goa Beaches',
            description='Explore the beautiful beaches of Goa with golden sands and clear blue waters. Perfect for relaxation and water sports.',
            price=15000,
            duration='5 Days / 4 Nights',
            location='Goa',
            category='beach'
        )
        goa.tags.add(beach_tag, luxury_tag)
        
        kerala = Destination.objects.create(
            name='Kerala Backwaters',
            description='Experience the serene backwaters of Kerala in traditional houseboats. Enjoy the lush green landscapes and local cuisine.',
            price=20000,
            duration='7 Days / 6 Nights',
            location='Kerala',
            category='beach'
        )
        kerala.tags.add(family_tag, honeymoon_tag)
        
        # Create hotels
        Hotel.objects.create(
            name='Taj Exotica Resort & Spa',
            destination=goa,
            description='Luxury beachfront resort with spa, multiple pools, and fine dining options.',
            price_per_night=12000,
            rating=5
        ).amenities.add(wifi, pool, spa, restaurant, ac)
        
        Hotel.objects.create(
            name='The Leela Goa',
            destination=goa,
            description='5-star luxury resort with private beach, golf course, and Ayurvedic spa.',
            price_per_night=10000,
            rating=5
        ).amenities.add(wifi, pool, spa, restaurant, ac)
        
        Hotel.objects.create(
            name='Backwater Ripples',
            destination=kerala,
            description='Beautiful houseboat stay experience in Kerala backwaters with traditional Kerala meals.',
            price_per_night=8000,
            rating=4
        ).amenities.add(wifi, restaurant)

