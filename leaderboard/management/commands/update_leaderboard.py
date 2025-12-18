from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from leaderboard.models import UserStats


class Command(BaseCommand):
    help = 'Update all user stats for the leaderboard'

    def handle(self, *args, **options):
        users = User.objects.all()
        updated_count = 0

        for user in users:
            user_stats, created = UserStats.objects.get_or_create(user=user)
            user_stats.update_stats()
            updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully updated stats for {updated_count} users'
            )
        )
