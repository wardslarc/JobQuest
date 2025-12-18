# 🏆 Leaderboard Module Architecture Diagram

## System Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                           │
│                                                                 │
│  Home/Nav  Dashboard  Achievements  Leaderboard  Milestones    │
│    │          │             │           │            │         │
│    └──────────┴─────────────┴───────────┴────────────┘         │
│                           │                                    │
└───────────────────────────┼────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                        ROUTING LAYER                            │
│                    (resume/urls.py)                            │
│                                                                 │
│  /                    /leaderboard/                            │
│  ├─ admin/           ├─ (leaderboard_view)                    │
│  └─ resumeapp.urls   ├─ user/<username>/   (leaderboard_detail)│
│                      ├─ milestones/        (milestones_view)   │
│                      └─ stats/<type>/      (stats_by_filter)   │
└───────────────────────┬──────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────────┐
│                      VIEWS LAYER                                │
│                  (leaderboard/views.py)                        │
│                                                                 │
│  ┌─────────────────────┬──────────────────┬─────────────────┐  │
│  │ leaderboard_view()  │ leaderboard_detail_view()          │  │
│  │ • Get top 50        │ • Get user stats  • Get rank       │  │
│  │ • Add rankings      │ • Get apps        • Get milestones │  │
│  │ • Get current user  │ • Get breakdown                    │  │
│  └─────────────────────┴──────────────────┴─────────────────┘  │
│  ┌─────────────────────┬──────────────────────────────────────┐ │
│  │ milestones_view()   │ stats_by_filter_view()               │ │
│  │ • Get milestones    │ • Filter by XP/Apps/Offers/Achv    │ │
│  │ • Group by type     │ • Calculate ranks                  │ │
│  │ • Count stats       │ • Render filtered table            │ │
│  └─────────────────────┴──────────────────────────────────────┘ │
└───────────────────────┬──────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────────┐
│                    MODEL LAYER                                  │
│                (leaderboard/models.py)                         │
│                                                                 │
│  ┌──────────────────────┬──────────────────────────────────┐   │
│  │     UserStats        │        Milestone                 │   │
│  ├──────────────────────┼──────────────────────────────────┤   │
│  │ • user (OneToOne)    │ • user (ForeignKey)             │   │
│  │ • total_xp           │ • milestone_type                 │   │
│  │ • total_applications │ • title                          │   │
│  │ • total_offers       │ • description                    │   │
│  │ • total_achievements │ • value                          │   │
│  │ • level (1-6)        │ • achieved_at                    │   │
│  │ • last_updated       │                                  │   │
│  │                      │  MILESTONE TYPES:                │   │
│  │ METHODS:             │  • applications                  │   │
│  │ • calculate_level()  │  • offers                        │   │
│  │ • update_stats()     │  • xp                            │   │
│  └──────────────────────┴──────────────────────────────────┘   │
└───────────────────────┬──────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────────┐
│                  SIGNAL SYSTEM                                  │
│              (leaderboard/signals.py)                           │
│                                                                 │
│  Application Event  ──┬───────────────────┬──  Achievement      │
│  (create/update)      │                   │   Event             │
│                       ↓                   ↓   (unlock)          │
│                   Signal Fired        Signal Fired              │
│                       │                   │                     │
│                       └───────┬───────────┘                     │
│                               ↓                                 │
│                 UserStats.update_stats() Called                │
│                               │                                 │
│              ┌────────────────┼────────────────┐               │
│              ↓                ↓                 ↓               │
│        Calculate XP   Count Applications   Count Achievements  │
│              │                │                 │               │
│              └────────────────┼────────────────┘               │
│                               ↓                                 │
│                      Recalculate Level                         │
│                               │                                 │
│                               ↓                                 │
│                        Save to Database                        │
│                               │                                 │
│                               ↓                                 │
│                      Leaderboard Updated                       │
└─────────────────────────────────────────────────────────────────┘
```

## Database Schema

```
┌─────────────────────────────────────┐
│          auth_user                  │
├─────────────────────────────────────┤
│ id (PK)                             │
│ username                            │
│ email                               │
│ first_name                          │
│ last_name                           │
│ ...                                 │
└────────────┬────────────────────────┘
             │
             │ OneToOne
             │ (via leaderboard_stats)
             ↓
┌─────────────────────────────────────┐
│   leaderboard_userstats             │
├─────────────────────────────────────┤
│ id (PK)                             │
│ user_id (FK) ──── auth_user         │
│ total_xp                            │
│ total_applications                  │
│ total_offers                        │
│ total_achievements                  │
│ level                               │
│ last_updated                        │
│                                     │
│ Indexes: user_id, level, total_xp  │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│   leaderboard_milestone             │
├─────────────────────────────────────┤
│ id (PK)                             │
│ user_id (FK) ──── auth_user         │
│ milestone_type                      │
│ title                               │
│ description                         │
│ value                               │
│ achieved_at                         │
│                                     │
│ Indexes: user_id, milestone_type   │
└─────────────────────────────────────┘
```

## User Data Flow

```
1. USER POSTS APPLICATION
   │
   └─→ Application.objects.create(user=user, ...)
       │
       └─→ post_save signal triggered
           │
           └─→ get_or_create(UserStats, user=user)
               │
               └─→ update_stats()
                   ├─ Recalculate total_xp
                   ├─ Count applications
                   ├─ Count offers
                   ├─ Count achievements
                   ├─ Calculate level
                   └─ save()

2. USER UNLOCKS ACHIEVEMENT
   │
   └─→ UserAchievement.objects.create(user=user, achievement=ach)
       │
       └─→ post_save signal triggered
           │
           └─→ get_or_create(UserStats, user=user)
               │
               └─→ update_stats()
                   └─ Same as above

3. LEADERBOARD QUERIED
   │
   └─→ leaderboard_view()
       │
       ├─ UserStats.objects.all() [ordered by -total_xp]
       │
       ├─ Current user's stats
       │
       ├─ Add ranking (enumerate)
       │
       └─ Render template with:
           ├─ top_50_users
           ├─ current_user_stats
           ├─ current_user_rank
           └─ total_users_count
```

## View Context Structures

### leaderboard.html Context

```python
{
    'leaderboard_entries': [
        {
            'rank': 1,
            'user_stats': UserStats_obj,
            'is_current_user': True/False
        },
        ...
    ],
    'current_user_stats': UserStats_obj,
    'current_user_rank': int,
    'total_users': int
}
```

### user_detail.html Context

```python
{
    'profile_user': User_obj,
    'user_stats': UserStats_obj,
    'rank': int,
    'total_users': int,
    'applications': [Application_obj, ...],
    'milestones': [Milestone_obj, ...],
    'status_breakdown': {
        'wishlist': int,
        'applied': int,
        'interview': int,
        'offer': int,
        'rejected': int
    },
    'is_own_profile': True/False
}
```

## Template Rendering Flow

```
1. leaderboard.html
   ├─ Render header with filters
   ├─ Loop leaderboard_entries
   │  ├─ Calculate medal (🥇 🥈 🥉)
   │  ├─ Display rank, user, level, stats
   │  └─ Link to user profile
   └─ Show summary stats

2. user_detail.html
   ├─ Render user header
   ├─ Show rank/level/XP
   ├─ Show application breakdown
   ├─ List recent applications
   └─ List recent milestones

3. stats_filtered.html
   ├─ Render filter tabs
   ├─ Loop leaderboard_entries
   └─ Show metric-specific table

4. milestones.html
   ├─ Loop milestone types
   │  └─ Group and display milestones
   └─ Show stats summary
```

## Security Flow

```
Public Routes (No Auth Required):
├─ /leaderboard/ (Global rankings)
├─ /leaderboard/stats/xp/ (Filtered rankings)
└─ /leaderboard/stats/applications/
   /leaderboard/stats/offers/
   /leaderboard/stats/achievements/

Protected Routes (Auth Required):
├─ /leaderboard/user/<username>/ (@login_required)
└─ /leaderboard/milestones/ (@login_required)

Admin Routes (Admin Only):
└─ /admin/leaderboard/ (Django admin interface)
```

## Integration Points in Main App

```
resume/
├─ settings.py
│  └─ INSTALLED_APPS: add 'leaderboard'
│
├─ urls.py
│  └─ path('leaderboard/', include('leaderboard.urls'))
│
└─ templates/
   ├─ index.html
   │  └─ Add navbar link: {% url 'leaderboard:leaderboard' %}
   │
   └─ dashboard.html
      └─ Add 3 buttons:
         ├─ Leaderboard
         ├─ Milestones
         └─ Achievements (enhanced)
```

## Performance Considerations

```
Database Queries:
├─ Leaderboard page: 1-2 queries (UserStats)
├─ User detail: 3-4 queries (UserStats, Applications, Milestones)
└─ Admin: Full QuerySet with select_related

Caching Opportunities:
├─ Top 50 users (5-10 min cache)
├─ User profiles (1-5 min cache)
└─ Filter rankings (5-10 min cache)

Indexes Recommended:
├─ leaderboard_userstats.total_xp
├─ leaderboard_userstats.level
├─ leaderboard_milestone.user_id
└─ leaderboard_milestone.achieved_at
```

---

This architecture ensures:
✅ Scalable ranking system
✅ Real-time stats updates
✅ Responsive user interface
✅ Efficient database queries
✅ Secure access control
✅ Maintainable code structure
