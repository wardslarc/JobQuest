# Achievement System Guide

The Job Quest application features a comprehensive achievement system that gamifies your job search journey. Earn badges and accumulate points as you progress through different milestones!

## How Achievements Work

Achievements are automatically unlocked based on your actions in the application:

1. **Application Milestones** - Unlock badges when you reach certain numbers of applications
2. **Status Transitions** - Earn achievements when you move applications through different stages
3. **Diversity Badges** - Unlock achievements for applying to different positions and locations
4. **XP Rewards** - Earn points for specific achievements
5. **Speed Bonuses** - Get rewards for quick progression

## Available Achievements (17 Total)

### Application Count Achievements

- **First Step** (10 XP) - Add your first job application
- **Getting Started** (25 XP) - Add 5 job applications
- **On a Roll** (50 XP) - Add 10 job applications
- **Application Master** (100 XP) - Add 25 job applications

### Status-Based Achievements

- **First Submit** (20 XP) - Submit your first job application (move to "Applied")
- **Interview Incoming** (50 XP) - Receive your first interview (move to "Interview")
- **Multiple Interviews** (75 XP) - Get 5 interview opportunities
- **Dream Offer** (100 XP) - Receive your first job offer
- **Popular Candidate** (150 XP) - Receive 3 job offers
- **Persevere** (15 XP) - Receive your first rejection (but keep going!)
- **Resilient** (40 XP) - Get 5 rejections and keep applying

### Diversity Achievements

- **Wishlist Builder** (30 XP) - Add 10 companies to your wishlist
- **Jack of All Trades** (35 XP) - Apply for 5 different position types
- **Global Reach** (40 XP) - Apply to companies in 5 different locations

### Performance Achievements

- **Quick Mover** (50 XP) - Move an application to Interview within 7 days of creation
- **Century Club** (25 XP) - Accumulate 100 XP total
- **Thousands** (100 XP) - Accumulate 1,000 XP total

## How Points Work

Each achievement awards a fixed number of points:

- Small achievements: 10-30 points
- Medium achievements: 35-75 points
- Major achievements: 100-150 points

Your total points are displayed on the Achievements page and represent your overall progress in the job search gamification system.

## XP Calculation

XP is calculated based on your application statuses:

- **Wishlist**: 5 XP per application
- **Applied**: 20 XP per application
- **Interview**: 50 XP per application
- **Offer**: 100 XP per application
- **Rejected**: 10 XP per application

Total XP accumulates across all your applications.

## Accessing Your Achievements

1. Click on your profile dropdown (top right)
2. Select **Achievements**
3. View your unlocked badges with unlock dates
4. See your progress toward completion
5. Check how many points you've earned

## Achievement Checking Logic

The system checks for new achievements automatically when you:

- Add a new application
- Move an application to a different status (via drag-and-drop on the dashboard)

## Technical Details

### Models

- **Achievement**: Defines achievement properties (name, description, icon, points, criterion)
- **UserAchievement**: Tracks user-achievement relationships and unlock dates

### Views

- `achievements_view()`: Displays all achievements with unlock status and dates
- `check_all_achievements()`: Checks all 17 achievement criteria
- `check_and_unlock_achievement()`: Unlocks a single achievement

### Database

All achievement data is stored in the SQLite database and persists across sessions.

## Tips for Unlocking All Achievements

1. **Diversify Your Applications** - Apply to different positions and companies
2. **Expand Geographic Scope** - Target positions in multiple locations
3. **Be Strategic** - Move applications to later stages carefully to maintain high XP
4. **Stay Consistent** - Regular application activity increases your chances
5. **Speed is a Bonus** - Try to move applications to Interview status quickly

---

Achievement system created to motivate and reward your job search efforts! 🏆
