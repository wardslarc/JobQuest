# Leaderboard Module - Quick Start Guide

## Installation Complete! ✅

Your leaderboard module has been successfully created and integrated into your Job Quest application.

## What Was Created

### Core Components

- ✅ **Leaderboard App** - Full Django app with models, views, and templates
- ✅ **Database Models** - UserStats and Milestone models with auto-update signals
- ✅ **4 View Functions** - Leaderboard, user profiles, milestones, and filtered stats
- ✅ **4 Templates** - Fully responsive Tailwind CSS templates
- ✅ **URL Routes** - 4 routes under `/leaderboard/` prefix
- ✅ **Admin Interface** - Django admin panel for managing leaderboard data
- ✅ **Management Command** - `update_leaderboard` for batch updates

### Integration

- ✅ Added to `INSTALLED_APPS` in settings.py
- ✅ URL routes included in main urls.py
- ✅ Navigation links added to navbar
- ✅ Dashboard buttons added (Leaderboard, Milestones)
- ✅ Database migrations applied

## Quick Setup Steps

### 1. Initialize Existing User Data (Optional)

If you have existing users and applications, initialize their stats:

```bash
python manage.py update_leaderboard
```

Or use the shell:

```bash
python manage.py shell
>>> exec(open('leaderboard/initialize.py').read())
```

### 2. Create Test Data (Optional)

```python
python manage.py shell
>>> from django.contrib.auth.models import User
>>> from leaderboard.models import UserStats, Milestone
>>>
>>> # Stats are created automatically when users post applications
>>> # Just create applications in your dashboard!
```

### 3. Access the Leaderboard

**For Users:**

- Click "Leaderboard" in the navigation bar
- Or click "Leaderboard" button in your dashboard
- View rankings filtered by XP, Applications, Offers, or Achievements
- Click on any user to see their full profile

**For Admins:**

- Go to `/admin/leaderboard/`
- Manage UserStats and Milestones
- View detailed statistics

## How It Works

### Automatic Updates

Every time a user:

- ✅ Posts a new application → Stats updated
- ✅ Changes application status → Stats updated
- ✅ Unlocks an achievement → Stats updated
- ✅ Deletes an application → Stats updated

### Level Calculation

```
0-99 XP     → Level 1
100-499 XP  → Level 2
500-1499 XP → Level 3
1500-3499 XP → Level 4
3500-6999 XP → Level 5
7000+ XP    → Level 6
```

### XP Source

- Each application status has XP value:
  - Wishlist: 5 XP
  - Applied: 20 XP
  - Interview: 50 XP
  - Offer: 100 XP
  - Rejected: 10 XP
- Plus points from achievements

## Available Routes

| URL                                | Description               |
| ---------------------------------- | ------------------------- |
| `/leaderboard/`                    | Main leaderboard page     |
| `/leaderboard/user/<username>/`    | View user profile         |
| `/leaderboard/milestones/`         | View your milestones      |
| `/leaderboard/stats/xp/`           | Top users by XP           |
| `/leaderboard/stats/applications/` | Top users by applications |
| `/leaderboard/stats/offers/`       | Top users by offers       |
| `/leaderboard/stats/achievements/` | Top users by achievements |

## Management Commands

### Update All User Stats

```bash
python manage.py update_leaderboard
```

Use when:

- Initial setup with existing users
- Data inconsistencies detected
- After bulk application imports

## Files Overview

### Models (`leaderboard/models.py`)

- **UserStats**: Tracks user metrics, level, and XP
- **Milestone**: Records user achievements

### Views (`leaderboard/views.py`)

- `leaderboard_view()` - Global rankings
- `leaderboard_detail_view()` - User profile
- `milestones_view()` - User milestones
- `stats_by_filter_view()` - Filtered rankings

### Templates (`templates/leaderboard/`)

- `leaderboard.html` - Main rankings page
- `user_detail.html` - User profile page
- `stats_filtered.html` - Filtered rankings
- `milestones.html` - Milestone tracker

### Signals (`leaderboard/signals.py`)

- Auto-updates stats when data changes
- Keeps leaderboard synchronized

## Troubleshooting

### No data showing on leaderboard?

1. Run: `python manage.py update_leaderboard`
2. Post some applications to generate data
3. Stats update automatically within seconds

### Stats not updating?

1. Check `python manage.py check` for errors
2. Verify signals are enabled (check apps.py)
3. Try manual update: `python manage.py update_leaderboard`

### Admin access issues?

1. Create superuser: `python manage.py createsuperuser`
2. Go to `/admin/`
3. Navigate to Leaderboard section

## Next Steps

1. **Add Test Data**

   - Post applications through dashboard
   - Watch stats update in real-time

2. **Customize Styling**

   - Edit template files in `templates/leaderboard/`
   - All use Tailwind CSS classes

3. **Add Features**

   - Weekly/monthly leaderboards
   - Achievement badges
   - User profiles
   - Milestone notifications

4. **Monitor Performance**
   - Consider caching for large user bases
   - Add database indexes if needed

## Support

For issues or questions:

1. Check `leaderboard/README.md` for detailed documentation
2. Review `LEADERBOARD_INTEGRATION.md` for integration details
3. Check Django logs for signal errors

## Key Features Summary

🏆 **Global Rankings** - Compete with other users
📊 **Multiple Metrics** - Rank by XP, apps, offers, achievements
👤 **User Profiles** - View detailed stats for any user
🎯 **Milestones** - Track your progress
📈 **Level System** - Progress through 6 levels
⚡ **Auto-Update** - Stats update instantly
🎨 **Beautiful UI** - Responsive Tailwind design
🔐 **Secure** - Login required for profiles

---

**Happy Competing! 🚀**
