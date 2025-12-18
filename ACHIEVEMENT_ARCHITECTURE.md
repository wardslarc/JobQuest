# Achievement System - Technical Architecture

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTIONS                        │
│  (Add Application / Update Status via Dashboard)            │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              DJANGO VIEWS LAYER                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ add_application()                                      │ │
│  │ - Creates Application object                          │ │
│  │ - Calls: check_all_achievements(request.user)         │ │
│  │ - Returns: Redirect or JSON response                  │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ update_application_status()                            │ │
│  │ - Updates Application.status                           │ │
│  │ - Calls: check_all_achievements(request.user)         │ │
│  │ - Returns: JSON response                              │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ achievements_view()                                    │ │
│  │ - Queries all Achievements                            │ │
│  │ - Gets user's UserAchievements                        │ │
│  │ - Calculates progress & points                        │ │
│  │ - Renders achievements.html                          │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│         ACHIEVEMENT CHECKING LOGIC LAYER                    │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ check_all_achievements(user)                           │ │
│  │                                                        │ │
│  │ Query: Application.objects.filter(user=user)          │ │
│  │                                                        │ │
│  │ For each of 17 criteria:                              │ │
│  │ ├─ Check application volume (1, 5, 10, 25)          │ │
│  │ ├─ Check status progression (applied, interview...)  │ │
│  │ ├─ Check diversity (positions, locations, wishlist) │ │
│  │ ├─ Check XP accumulation (100, 1000)                │ │
│  │ └─ Check speed criteria (7-day window)              │ │
│  │                                                        │ │
│  │ For each matched criterion:                           │ │
│  │ └─ Call: check_and_unlock_achievement(user, criterion)│ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ check_and_unlock_achievement(user, criterion)         │ │
│  │                                                        │ │
│  │ 1. Query: Achievement.objects.get(criterion=criterion)│ │
│  │ 2. Check: UserAchievement.objects.filter(             │ │
│  │    user=user, achievement=achievement).exists()      │ │
│  │ 3. If not exists:                                     │ │
│  │    └─ Create: UserAchievement(user, achievement)     │ │
│  │ 4. Return: Success/Failure boolean                    │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              DATABASE LAYER                                 │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ APPLICATION TABLE                                     │ │
│  │ ├─ id (PK)                                           │ │
│  │ ├─ user_id (FK)                                      │ │
│  │ ├─ company                                           │ │
│  │ ├─ position                                          │ │
│  │ ├─ status (wishlist|applied|interview|offer|rejected)│ │
│  │ ├─ salary                                            │ │
│  │ ├─ location                                          │ │
│  │ ├─ notes                                             │ │
│  │ ├─ created_at                                        │ │
│  │ └─ updated_at                                        │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ ACHIEVEMENT TABLE                                     │ │
│  │ ├─ id (PK)                                           │ │
│  │ ├─ name (UNIQUE)                                     │ │
│  │ ├─ description                                       │ │
│  │ ├─ icon_class (Font Awesome)                         │ │
│  │ ├─ color_class (Tailwind gradient)                   │ │
│  │ ├─ points (integer)                                  │ │
│  │ ├─ criterion (UNIQUE trigger identifier)             │ │
│  │ └─ created_at                                        │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ USER_ACHIEVEMENT TABLE (M2M)                          │ │
│  │ ├─ id (PK)                                           │ │
│  │ ├─ user_id (FK) + achievement_id (FK) [UNIQUE]       │ │
│  │ └─ unlocked_at                                       │ │
│  │                                                        │ │
│  │ UNIQUE CONSTRAINT: (user_id, achievement_id)         │ │
│  │ Ensures: Each user can only unlock each achievement  │ │
│  │          once (prevents duplicates)                  │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              TEMPLATE LAYER (Frontend)                      │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ achievements.html                                     │ │
│  │                                                        │ │
│  │ Context Variables Received:                           │ │
│  │ ├─ achievements (list of dicts)                       │ │
│  │ ├─ unlocked_count (int)                              │ │
│  │ ├─ total_count (int)                                 │ │
│  │ ├─ completion_percentage (int)                       │ │
│  │ └─ total_points (int)                                │ │
│  │                                                        │ │
│  │ Renders:                                              │ │
│  │ ├─ Progress card with bar                            │ │
│  │ ├─ Achievement grid (responsive)                     │ │
│  │ ├─ Individual achievement cards with:                │ │
│  │ │  ├─ Icon & gradient                               │ │
│  │ │  ├─ Name & description                            │ │
│  │ │  ├─ Points value                                  │ │
│  │ │  ├─ Unlock status badge                           │ │
│  │ │  └─ Unlock date (if applicable)                   │ │
│  │ └─ Motivational banner                              │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Flow: Adding Application → Achievement Unlock

```
User clicks "Add Application"
                │
                ▼
        HTML Form Submitted (POST)
                │
                ▼
        Django View: add_application()
                │
                ├─ Validate form data
                │
                ├─ Create Application object
                │   └─ app = Application.objects.create(...)
                │
                ├─ Call: check_all_achievements(request.user)
                │   │
                │   ├─ Query all user applications
                │   │
                │   ├─ Check criterion #1: application_count == 1
                │   │   │
                │   │   ├─ If TRUE → Call: check_and_unlock_achievement(
                │   │   │              user, 'first_application')
                │   │   │   │
                │   │   │   ├─ Query Achievement where criterion='first_application'
                │   │   │   │
                │   │   │   ├─ Check: UserAchievement exists?
                │   │   │   │   └─ If NO → Create UserAchievement record
                │   │   │   │       (timestamp recorded as unlocked_at)
                │   │   │   │
                │   │   │   └─ Return: True (achievement unlocked)
                │   │   │
                │   │   └─ If FALSE → Continue to next criterion
                │   │
                │   ├─ Check criterion #2-#17: (similar process)
                │   │
                │   └─ Return from check_all_achievements()
                │
                ├─ Save success message
                │
                └─ Return response
                    │
                    ├─ If standard POST → Redirect to dashboard
                    └─ If AJAX → Return JSON {success: true}

User redirected to dashboard
                │
                ▼
User clicks "Achievements" in dropdown
                │
                ▼
        Django View: achievements_view()
                │
                ├─ Query: all Achievements
                │
                ├─ Query: UserAchievements for this user
                │
                ├─ Build achievements_data list:
                │   For each achievement:
                │   ├─ Check if user has unlocked it
                │   ├─ Get unlock date (if applicable)
                │   └─ Add to list
                │
                ├─ Calculate:
                │   ├─ unlocked_count
                │   ├─ total_count
                │   ├─ completion_percentage
                │   └─ total_points
                │
                └─ Render achievements.html with context

Template displays achievements page
                │
                ▼
User sees:
├─ Progress card showing 5% (1 of 17 achievements)
├─ Achievement grid with cards
├─ First achievement "First Step" marked as "Unlocked!"
├─ Unlock date displayed: "Jan 15, 2025"
└─ Other achievements shown as locked/grayed out
```

---

## Database Query Patterns

### Query Pattern 1: Get All User Applications (Efficient)

```python
applications = Application.objects.filter(user=user)
```

**Single query**: Retrieves all applications for user with single database hit.

### Query Pattern 2: Check Achievement Criterion

```python
# Application count
count = applications.count()

# Status count
interview_count = applications.filter(status='interview').count()

# Distinct positions
unique_positions = applications.values('position').distinct().count()

# Total XP
total_xp = sum(app.get_xp() for app in applications)
```

**Efficient**: All calculated from single applications query result.

### Query Pattern 3: Unlock Achievement

```python
try:
    achievement = Achievement.objects.get(criterion=criterion)
    obj, created = UserAchievement.objects.get_or_create(
        user=user,
        achievement=achievement
    )
    return created
except Achievement.DoesNotExist:
    return False
```

**Atomic**: `get_or_create` ensures no race conditions or duplicates.

---

## Achievement Criteria Evaluation Logic

```
check_all_achievements(user):

    applications = user.applications (1 query)

    ▶ Milestone 1: application_count
        if count == 1: unlock 'first_application'
        if count == 5: unlock 'five_applications'
        if count == 10: unlock 'ten_applications'
        if count == 25: unlock 'twenty_five_applications'

    ▶ Milestone 2: status transitions (first occurrence)
        if any status='applied': unlock 'first_applied'
        if any status='interview': unlock 'first_interview'
        if any status='offer': unlock 'first_offer'
        if any status='rejected': unlock 'first_rejection'

    ▶ Milestone 3: status counts (accumulation)
        if count(status='interview') >= 5: unlock 'five_interviews'
        if count(status='offer') >= 3: unlock 'three_offers'
        if count(status='rejected') >= 5: unlock 'five_rejections'
        if count(status='wishlist') >= 10: unlock 'ten_wishlist'

    ▶ Milestone 4: diversity metrics
        if distinct(position) >= 5: unlock 'five_positions'
        if distinct(location) >= 5: unlock 'five_locations'

    ▶ Milestone 5: xp accumulation
        total_xp = sum(app.get_xp() for app in applications)
        if total_xp >= 100: unlock 'hundred_xp'
        if total_xp >= 1000: unlock 'thousand_xp'

    ▶ Milestone 6: time-based (speed rewards)
        if any(status='interview' AND created_at > now-7days):
            unlock 'quick_interview'
```

---

## Key Design Patterns Used

### 1. **Separation of Concerns**

```
Views Layer       → Handle HTTP requests/responses
Logic Layer       → Achievement checking functions
Database Layer    → Models and ORM queries
Template Layer    → Presentation of achievements
```

### 2. **Single Responsibility**

```
check_all_achievements()       → Orchestrates all checks
check_and_unlock_achievement() → Unlocks single achievement
Achievement model              → Stores achievement data
UserAchievement model          → Stores unlock relationships
```

### 3. **DRY (Don't Repeat Yourself)**

```
Unique constraint on Achievement.criterion prevents duplicates
Unique constraint on UserAchievement prevents duplicate unlocks
check_and_unlock_achievement() reused for all 17 criteria
```

### 4. **Idempotency**

```
Running check_all_achievements() multiple times is safe
✓ Uses get_or_create() for atomic operations
✓ Checks existing unlocks before creating new ones
✓ No side effects from multiple executions
```

---

## Performance Characteristics

### Time Complexity

```
check_all_achievements(user):
- Query applications:        O(1) single database query
- Evaluate criteria:         O(1) in-memory calculations
- Unlock achievement:        O(1) per criterion lookup + create
- Total:                     O(1) constant time regardless of app count
```

### Space Complexity

```
check_all_achievements(user):
- Store applications:        O(n) where n = user's apps
- Store calculations:        O(1) constant variables
- Total:                     O(n) linear in application count
```

### Database Queries

```
Per achievement check:
1. Application.objects.filter(user=user)
2. Achievement.objects.get(criterion=criterion)  [cached after first]
3. UserAchievement.objects.get_or_create(user, achievement)

Total queries: ~5-10 per check_all_achievements() call
Queries could be optimized with SELECT_RELATED/PREFETCH_RELATED if needed
```

---

## Security Considerations

### User Isolation

```python
# Always filter by user
applications = Application.objects.filter(user=user)
user_achievements = UserAchievement.objects.filter(user=user)
```

✅ Prevents unauthorized access to other users' data

### Input Validation

```python
@login_required
def achievements_view(request):
    # Ensures only authenticated users access achievements
```

✅ Achievement data only visible to logged-in users

### Unique Constraints

```python
# UserAchievement model
class Meta:
    unique_together = ['user', 'achievement']
```

✅ Prevents duplicate achievement unlocks

### CSRF Protection

```html
{% csrf_token %}
<!-- In all forms -->
```

✅ Protects against cross-site attacks

---

## Extensibility

### Adding New Achievements

```python
# 1. Create Achievement in admin or management command
# 2. Add criterion to Achievement
# 3. Add logic to check_all_achievements()
# 4. Achievement automatically appears and checks

# No changes needed to views or models!
```

### Modifying Criteria

```python
# Change points value → Update Achievement record
# Change icon → Update Achievement.icon_class
# Change criterion logic → Update check_all_achievements()

# All backward compatible!
```

### Adding Unlock Notifications

```python
# In check_and_unlock_achievement():
if unlock_success:
    # Send notification signal
    achievement_unlocked.send(sender=Achievement, user=user, ...)
```

---

This architecture ensures the achievement system is:

- ✅ Scalable to thousands of users
- ✅ Maintainable and extensible
- ✅ Performant with minimal database queries
- ✅ Secure with proper user isolation
- ✅ Robust with atomic operations
