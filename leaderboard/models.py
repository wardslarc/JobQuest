from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from resumeapp.models import Application, UserAchievement


class UserStats(models.Model):
    """Track user statistics for leaderboard rankings"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard_stats')
    total_xp = models.IntegerField(default=0)
    total_applications = models.IntegerField(default=0)
    total_offers = models.IntegerField(default=0)
    total_achievements = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-total_xp']
        verbose_name = "User Stats"
        verbose_name_plural = "User Stats"
    
    def __str__(self):
        return f"{self.user.username} - Level {self.level} ({self.total_xp} XP)"
    
    @classmethod
    def calculate_level(cls, xp):
        """Calculate level based on XP"""
        if xp < 100:
            return 1
        elif xp < 500:
            return 2
        elif xp < 1500:
            return 3
        elif xp < 3500:
            return 4
        elif xp < 7000:
            return 5
        else:
            return 6
    
    def update_stats(self):
        """Update all stats for the user"""
        applications = Application.objects.filter(user=self.user)
        
        # Calculate total XP
        self.total_xp = sum(app.get_xp() for app in applications) + (
            UserAchievement.objects.filter(user=self.user).aggregate(
                total=Sum('achievement__points')
            )['total'] or 0
        )
        
        # Count applications
        self.total_applications = applications.count()
        self.total_offers = applications.filter(status='offer').count()
        
        # Count achievements
        self.total_achievements = UserAchievement.objects.filter(user=self.user).count()
        
        # Calculate level
        self.level = self.calculate_level(self.total_xp)
        
        self.save()


class Milestone(models.Model):
    """Track milestones achieved by users"""
    MILESTONE_TYPES = [
        ('applications', 'Applications Posted'),
        ('offers', 'Offers Received'),
        ('xp', 'XP Milestone'),
        ('achievements', 'Achievements Unlocked'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='milestones')
    milestone_type = models.CharField(max_length=20, choices=MILESTONE_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    value = models.IntegerField()  # e.g., 10 applications, 5 offers
    achieved_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-achieved_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
