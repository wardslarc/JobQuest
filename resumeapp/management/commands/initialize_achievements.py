from django.core.management.base import BaseCommand
from resumeapp.models import Achievement


class Command(BaseCommand):
    help = 'Initialize achievements'

    def handle(self, *args, **options):
        achievements = [
            {
                'name': 'First Step',
                'description': 'Add your first job application',
                'icon_class': 'fa-paper-plane',
                'color_class': 'from-blue-500 to-blue-600',
                'points': 10,
                'criterion': 'first_application'
            },
            {
                'name': 'Getting Started',
                'description': 'Add 5 job applications',
                'icon_class': 'fa-rocket',
                'color_class': 'from-purple-500 to-purple-600',
                'points': 25,
                'criterion': 'five_applications'
            },
            {
                'name': 'On a Roll',
                'description': 'Add 10 job applications',
                'icon_class': 'fa-fire',
                'color_class': 'from-orange-500 to-orange-600',
                'points': 50,
                'criterion': 'ten_applications'
            },
            {
                'name': 'Application Master',
                'description': 'Add 25 job applications',
                'icon_class': 'fa-crown',
                'color_class': 'from-yellow-500 to-yellow-600',
                'points': 100,
                'criterion': 'twenty_five_applications'
            },
            {
                'name': 'First Submit',
                'description': 'Submit your first job application',
                'icon_class': 'fa-check-circle',
                'color_class': 'from-green-500 to-green-600',
                'points': 20,
                'criterion': 'first_applied'
            },
            {
                'name': 'Interview Incoming',
                'description': 'Receive your first interview',
                'icon_class': 'fa-video',
                'color_class': 'from-pink-500 to-pink-600',
                'points': 50,
                'criterion': 'first_interview'
            },
            {
                'name': 'Multiple Interviews',
                'description': 'Get 5 interview opportunities',
                'icon_class': 'fa-star',
                'color_class': 'from-purple-500 to-purple-600',
                'points': 75,
                'criterion': 'five_interviews'
            },
            {
                'name': 'Dream Offer',
                'description': 'Receive your first job offer',
                'icon_class': 'fa-trophy',
                'color_class': 'from-red-500 to-red-600',
                'points': 100,
                'criterion': 'first_offer'
            },
            {
                'name': 'Popular Candidate',
                'description': 'Receive 3 job offers',
                'icon_class': 'fa-gems',
                'color_class': 'from-yellow-500 to-yellow-600',
                'points': 150,
                'criterion': 'three_offers'
            },
            {
                'name': 'Persevere',
                'description': 'Receive your first rejection (but keep going!)',
                'icon_class': 'fa-shield-alt',
                'color_class': 'from-blue-500 to-blue-600',
                'points': 15,
                'criterion': 'first_rejection'
            },
            {
                'name': 'Resilient',
                'description': 'Get 5 rejections and keep applying',
                'icon_class': 'fa-heart',
                'color_class': 'from-pink-500 to-pink-600',
                'points': 40,
                'criterion': 'five_rejections'
            },
            {
                'name': 'Wishlist Builder',
                'description': 'Add 10 companies to your wishlist',
                'icon_class': 'fa-heart',
                'color_class': 'from-red-500 to-red-600',
                'points': 30,
                'criterion': 'ten_wishlist'
            },
            {
                'name': 'Jack of All Trades',
                'description': 'Apply for 5 different position types',
                'icon_class': 'fa-briefcase',
                'color_class': 'from-green-500 to-green-600',
                'points': 35,
                'criterion': 'five_positions'
            },
            {
                'name': 'Global Reach',
                'description': 'Apply to companies in 5 different locations',
                'icon_class': 'fa-globe',
                'color_class': 'from-blue-500 to-blue-600',
                'points': 40,
                'criterion': 'five_locations'
            },
            {
                'name': 'Quick Mover',
                'description': 'Move an application from Wishlist to Interview within 7 days',
                'icon_class': 'fa-lightning-bolt',
                'color_class': 'from-yellow-500 to-yellow-600',
                'points': 50,
                'criterion': 'quick_interview'
            },
            {
                'name': 'Century Club',
                'description': 'Accumulate 100 XP',
                'icon_class': 'fa-star',
                'color_class': 'from-purple-500 to-purple-600',
                'points': 25,
                'criterion': 'hundred_xp'
            },
            {
                'name': 'Thousands',
                'description': 'Accumulate 1000 XP',
                'icon_class': 'fa-crown',
                'color_class': 'from-red-500 to-red-600',
                'points': 100,
                'criterion': 'thousand_xp'
            },
        ]

        for ach in achievements:
            Achievement.objects.get_or_create(
                name=ach['name'],
                defaults={
                    'description': ach['description'],
                    'icon_class': ach['icon_class'],
                    'color_class': ach['color_class'],
                    'points': ach['points'],
                    'criterion': ach['criterion']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully initialized achievements'))
