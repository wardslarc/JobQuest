from django.core.management.base import BaseCommand
from leaderboard.models import UserStats
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Recalculate all user stats in the leaderboard'

    def add_arguments(self, parser):
        parser.add_argument(
            '--user',
            type=str,
            help='Recalculate stats for a specific username',
        )

    def handle(self, *args, **options):
        if options['user']:
            try:
                user = User.objects.get(username=options['user'])
                user_stats, created = UserStats.objects.get_or_create(user=user)
                user_stats.update_stats()
                user_stats.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully recalculated stats for {user.username}'
                    )
                )
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'User {options["user"]} not found')
                )
        else:
            users = User.objects.all()
            count = 0
            for user in users:
                user_stats, created = UserStats.objects.get_or_create(user=user)
                user_stats.update_stats()
                user_stats.save()
                count += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully recalculated stats for {count} users'
                )
            )
