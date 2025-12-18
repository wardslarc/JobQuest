# Leaderboard Module Documentation

The Leaderboard module is a comprehensive ranking and statistics tracking system for the Job Quest application. It tracks user progress, rankings, and achievements in a competitive and gamified environment.

## Features

### 1. **User Statistics Tracking**

- **Total XP**: Accumulated experience points from applications and achievements
- **Total Applications**: Count of all job applications posted
- **Total Offers**: Count of successful offers received
- **Total Achievements**: Count of unlocked achievements
- **Level System**: Users are ranked into 6 levels based on XP:
  - Level 1: 0-99 XP
  - Level 2: 100-499 XP
  - Level 3: 500-1499 XP
  - Level 4: 1500-3499 XP
  - Level 5: 3500-6999 XP
  - Level 6: 7000+ XP

### 2. **Global Leaderboard**

- View the top 50 users ranked by XP
- Filterable rankings by:
  - XP (Total experience)
  - Applications (Most applications posted)
  - Offers (Most offers received)
  - Achievements (Most achievements unlocked)
- Current user's rank and position highlighted
- User profiles with detailed statistics

### 3. **User Profiles**

Each user profile includes:

- Global rank and tier
- Level and total XP
- Application statistics breakdown
- Recent applications
- Recent milestones achieved
- Success rate calculation

### 4. **Milestone Tracking**

Users can earn milestones for:

- **Applications**: Posting applications (e.g., "10 Applications Posted")
- **Offers**: Receiving job offers (e.g., "5 Offers Received")
- **XP**: Reaching XP milestones (e.g., "1000 XP Reached")
- **Achievements**: Unlocking achievements (e.g., "5 Achievements Unlocked")

## Database Models

### UserStats

```python
class UserStats(models.Model):
    user              # OneToOne: Connected user
    total_xp          # Total experience points
    total_applications # Count of applications
    total_offers      # Count of offers
    total_achievements # Count of achievements
    level             # Current level (1-6)
    last_updated      # Last update timestamp
```

### Milestone

```python
class Milestone(models.Model):
    user              # Foreign Key: User who achieved milestone
    milestone_type    # Type: applications, offers, xp, achievements
    title             # Milestone title
    description       # Milestone description
    value             # Numerical value
    achieved_at       # Timestamp of achievement
```

## URL Endpoints

- `/leaderboard/` - Main leaderboard page (Top 50 users)
- `/leaderboard/user/<username>/` - User profile page
- `/leaderboard/milestones/` - Current user's milestones
- `/leaderboard/stats/<filter_type>/` - Filtered leaderboard by stat type

## Auto-Update Features

The module automatically updates user statistics when:

- An application is created or updated
- An application is deleted
- An achievement is unlocked
- An achievement is revoked

This is handled through Django signals in `signals.py`.

## Management Commands

### update_leaderboard

Updates all user statistics in the leaderboard.

```bash
python manage.py update_leaderboard
```

Use this command to:

- Initial population of leaderboard data
- Fix inconsistent stats
- Recalculate all rankings

## Integration Points

The leaderboard is integrated into:

1. **Navigation**: Links available from main navigation and dashboard
2. **Dashboard**: Quick access buttons to leaderboard, milestones, and achievements
3. **User Profiles**: View other users' statistics and milestones
4. **Admin Panel**: Manage user stats and milestones

## Templates

- `leaderboard/leaderboard.html` - Main leaderboard view
- `leaderboard/user_detail.html` - User profile page
- `leaderboard/stats_filtered.html` - Filtered statistics page
- `leaderboard/milestones.html` - Milestone tracker

## Admin Interface

The Django admin interface provides:

- View and filter user statistics
- Search users by username or email
- View milestone history
- Edit user levels and XP (for administration)

Access at `/admin/leaderboard/`

## API Response Structure

### Leaderboard Entry

```python
{
    'rank': int,
    'user_stats': UserStats,
    'is_current_user': bool
}
```

### User Stats Context

```python
{
    'leaderboard_entries': list,
    'current_user_stats': UserStats,
    'current_user_rank': int,
    'total_users': int
}
```

## Future Enhancement Ideas

1. Weekly/Monthly leaderboards
2. Achievements for streaks
3. Social features (following users)
4. Badges system
5. Leaderboard notifications
6. Team/cohort leaderboards
7. XP multipliers for special events
8. Seasonal rankings

## Notes

- Stats are updated automatically through signals
- User must be authenticated to view detailed profiles
- Public leaderboard is visible to all users
- Each user has a maximum of one UserStats record (OneToOne relationship)
