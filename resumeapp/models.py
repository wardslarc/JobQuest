from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    STATUS_CHOICES = [
        ('wishlist', 'Wishlist'),
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ]
    
    XP_VALUES = {
        'wishlist': 5,
        'applied': 20,
        'interview': 50,
        'offer': 100,
        'rejected': 10,
    }
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')
    salary = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    def get_xp(self):
        return self.XP_VALUES.get(self.status, 0)


class Achievement(models.Model):
    ICON_CHOICES = [
        ('fa-star', 'Star'),
        ('fa-fire', 'Fire'),
        ('fa-rocket', 'Rocket'),
        ('fa-target', 'Target'),
        ('fa-gem', 'Gem'),
        ('fa-trophy', 'Trophy'),
        ('fa-crown', 'Crown'),
        ('fa-lightning-bolt', 'Lightning'),
    ]
    
    COLOR_CHOICES = [
        ('from-blue-500 to-blue-600', 'Blue'),
        ('from-purple-500 to-purple-600', 'Purple'),
        ('from-green-500 to-green-600', 'Green'),
        ('from-pink-500 to-pink-600', 'Pink'),
        ('from-orange-500 to-orange-600', 'Orange'),
        ('from-red-500 to-red-600', 'Red'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=30, choices=ICON_CHOICES)
    color_class = models.CharField(max_length=50, choices=COLOR_CHOICES)
    points = models.IntegerField(default=10)
    criterion = models.CharField(max_length=50, help_text="Trigger condition: e.g., 'first_application', 'five_applications', 'offer_received'")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    unlocked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'achievement']
        ordering = ['-unlocked_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"

