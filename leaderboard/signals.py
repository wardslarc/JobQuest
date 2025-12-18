from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from resumeapp.models import Application, UserAchievement
from .models import UserStats


@receiver(post_save, sender=Application)
def update_stats_on_application_save(sender, instance, created, **kwargs):
    """Update user stats when an application is created or updated"""
    user_stats, _ = UserStats.objects.get_or_create(user=instance.user)
    user_stats.update_stats()
    user_stats.save(update_fields=['total_xp', 'total_applications', 'total_offers', 'level'])


@receiver(post_delete, sender=Application)
def update_stats_on_application_delete(sender, instance, **kwargs):
    """Update user stats when an application is deleted"""
    try:
        user_stats = UserStats.objects.get(user=instance.user)
        user_stats.update_stats()
        user_stats.save(update_fields=['total_xp', 'total_applications', 'total_offers', 'level'])
    except UserStats.DoesNotExist:
        pass


@receiver(post_save, sender=UserAchievement)
def update_stats_on_achievement_save(sender, instance, created, **kwargs):
    """Update user stats when an achievement is unlocked"""
    user_stats, _ = UserStats.objects.get_or_create(user=instance.user)
    user_stats.update_stats()
    user_stats.save(update_fields=['total_xp', 'total_achievements', 'level'])


@receiver(post_delete, sender=UserAchievement)
def update_stats_on_achievement_delete(sender, instance, **kwargs):
    """Update user stats when an achievement is revoked"""
    try:
        user_stats = UserStats.objects.get(user=instance.user)
        user_stats.update_stats()
        user_stats.save(update_fields=['total_xp', 'total_achievements', 'level'])
    except UserStats.DoesNotExist:
        pass
