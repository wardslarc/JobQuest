"""
Initialize Leaderboard Module

This script helps initialize the leaderboard for existing users in the system.
Run this after installing the leaderboard module to populate initial stats.

Usage:
    python manage.py shell
    >>> exec(open('leaderboard/initialize.py').read())
"""

from django.contrib.auth.models import User
from leaderboard.models import UserStats

def initialize_leaderboard():
    """Initialize leaderboard stats for all existing users"""
    users = User.objects.all()
    created_count = 0
    updated_count = 0
    
    print(f"Initializing leaderboard for {users.count()} users...")
    
    for user in users:
        user_stats, created = UserStats.objects.get_or_create(user=user)
        user_stats.update_stats()
        
        if created:
            created_count += 1
            print(f"✓ Created stats for {user.username}")
        else:
            updated_count += 1
            print(f"✓ Updated stats for {user.username}")
    
    print(f"\n✅ Initialization complete!")
    print(f"   Created: {created_count} new stat records")
    print(f"   Updated: {updated_count} existing stat records")
    
    # Show top users
    print("\n📊 Top 5 Users:")
    top_users = UserStats.objects.all()[:5]
    for rank, stats in enumerate(top_users, 1):
        print(f"   {rank}. {stats.user.first_name} (Level {stats.level}, {stats.total_xp} XP)")

if __name__ == '__main__':
    initialize_leaderboard()
