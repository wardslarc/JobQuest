# Job Quest - Gamified Job Search Application

A comprehensive Django-based job search application with gamification features including achievements, milestones, leaderboards, and an interactive kanban dashboard to track your job applications.

## 🎯 Features

### 📱 Application Management

- **Kanban Dashboard** - Drag-and-drop interface to manage applications across 5 statuses: Wishlist, Applied, Interview, Offer, Rejected
- **Real-time Status Updates** - AJAX-powered status changes with visual feedback
- **Application Details** - Track company, position, location, salary, and notes for each application
- **Quick Stats** - View summary statistics of applications by status

### 🏆 Achievement System

- **17 Unique Achievements** - Earn badges as you progress through your job search
- **Automatic Unlocking** - Achievements unlock based on your actions (applications, status changes, milestones)
- **Progress Tracking** - Visual progress bar showing achievement completion percentage
- **Points System** - Each achievement awards points toward your total score
- **Unlock Dates** - Track exactly when each achievement was earned

**Achievement Categories:**

- **Volume Milestones** - First Step, Getting Started, On a Roll, Application Master
- **Status Progression** - First Submit, Interview Incoming, Multiple Interviews, Dream Offer, Popular Candidate, Persevere, Resilient
- **Diversity Rewards** - Wishlist Builder, Jack of All Trades, Global Reach
- **Performance Bonuses** - Quick Mover, Century Club, Thousands

### 🎯 Milestone Tracking

- **Automatic Milestone Creation** - Track major achievements like applications posted, offers received, XP milestones, and achievements unlocked
- **Milestone Dashboard** - View recent milestones with type-specific icons and values
- **Detailed Milestone Page** - Complete history of all milestones achieved
- **Summary Statistics** - Quick overview of latest values for each milestone type

### 🏅 Leaderboards

- **Global Rankings** - Compete with other users based on achievements and milestones
- **User Profiles** - View other users' achievement progress and recent milestones
- **Achievement Comparison** - See who has unlocked which achievements
- **Performance Metrics** - Track progress through various metrics

### 👤 User Management

- **User Authentication** - Secure signup and login with email verification
- **Profile Management** - View and update user information
- **Settings** - Change username and password
- **Theme Switching** - Light, dark, and system theme options

### 🎨 User Interface

- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- **Dark Mode Support** - Comfortable viewing in any lighting condition
- **Tailwind CSS** - Modern utility-first styling
- **Font Awesome Icons** - Beautiful icons throughout the application
- **Smooth Animations** - Delightful transitions and interactions

## 🛠️ Technology Stack

### Backend

- **Django 6.0** - Python web framework
- **Python 3.14** - Programming language
- **SQLite** - Database

### Frontend

- **HTML5** - Markup
- **Tailwind CSS 3.4.19** - Utility-first CSS framework
- **JavaScript (Vanilla)** - Interactivity and drag-drop functionality
- **Font Awesome 6.4.0** - Icon library

### Key Libraries

- **django-cors-headers** - CORS handling
- **sqlparse** - SQL parsing
- **asgiref** - ASGI utilities
- **tzdata** - Timezone data

## 📋 Project Structure

```
resume/
├── manage.py                 # Django management script
├── db.sqlite3               # Database
├── package.json             # NPM dependencies
├── tailwind.config.js       # Tailwind CSS configuration
├── postcss.config.js        # PostCSS configuration
│
├── resume/                  # Main Django project
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── resumeapp/               # Main application
│   ├── models.py            # Database models (Application, Achievement, UserAchievement)
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Django admin configuration
│   ├── management/
│   │   └── commands/
│   │       └── initialize_achievements.py  # Management command to seed achievements
│   ├── migrations/          # Database migrations
│   └── __pycache__/
│
├── leaderboard/             # Leaderboard and milestones app
│   ├── models.py            # Milestone model
│   ├── views.py             # Leaderboard views
│   ├── urls.py              # Leaderboard URLs
│   ├── signals.py           # Signal handlers for milestone creation
│   ├── initialize.py        # Initialization utilities
│   └── migrations/
│
├── static/                  # Static files
│   └── css/
│       ├── tailwind.css     # Main stylesheet
│       └── input.css        # Tailwind input
│
├── templates/               # HTML templates
│   ├── index.html           # Base template with navigation
│   ├── dashboard.html       # Main kanban dashboard
│   ├── login.html           # Login page
│   ├── signup.html          # Signup page
│   ├── profile.html         # User profile
│   ├── achievements.html    # Full achievements page
│   ├── achievementssection.html      # Achievement widget for dashboard
│   ├── milestones.html      # Milestones page
│   ├── milestonessection.html        # Milestone widget for dashboard
│   ├── leaderboard_main.html         # Leaderboard page
│   ├── user_detail.html     # User detail page
│   └── addApplication.html  # Add application modal
│
└── env/                     # Virtual environment
```

## 🚀 Installation

### Prerequisites

- Python 3.14+
- pip (Python package manager)
- Node.js (for Tailwind CSS)

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/job-quest.git
cd job-quest/resume
```

2. **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install Python dependencies**

```bash
pip install -r requirements.txt
```

4. **Install Node dependencies** (for Tailwind CSS)

```bash
npm install
```

5. **Initialize the database**

```bash
python manage.py migrate
```

6. **Initialize achievements**

```bash
python manage.py initialize_achievements
```

7. **Create a superuser** (optional, for admin panel)

```bash
python manage.py createsuperuser
```

8. **Build Tailwind CSS**

```bash
npm run build
```

## 🏃 Running the Application

### Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

### Watch Tailwind CSS (for development)

```bash
npm run dev
```

## 📖 Usage Guide

### Getting Started

1. **Sign Up** - Create a new account with email and password
2. **Add Applications** - Click "Add Application" to track a new job opportunity
3. **Manage Status** - Drag applications between columns to update their status
4. **Track Progress** - View achievements and milestones earned

### Dashboard

- **Stats Cards** - See summary of applications by status
- **Kanban Board** - Manage applications with drag-and-drop
- **Achievement Progress** - Track unlocked achievements
- **Recent Milestones** - View latest milestones achieved

### Achievements Page

- View all 17 available achievements
- See unlock dates for earned achievements
- Track your progress toward completion
- View total points earned

### Milestones Page

- Complete history of achievements
- Grouped by milestone type (Applications, Offers, XP, Achievements)
- Detailed timestamp information

### Leaderboard

- Compare progress with other users
- View global rankings
- See who has unlocked specific achievements

## 🎮 Achievement Categories

### Volume Achievements (4)

- **First Step** (10 XP) - Add your first application
- **Getting Started** (25 XP) - Add 5 applications
- **On a Roll** (50 XP) - Add 10 applications
- **Application Master** (100 XP) - Add 25 applications

### Status Progression (7)

- **First Submit** (20 XP) - Submit your first application
- **Interview Incoming** (50 XP) - Receive your first interview
- **Multiple Interviews** (75 XP) - Get 5 interviews
- **Dream Offer** (100 XP) - Receive your first offer
- **Popular Candidate** (150 XP) - Receive 3 offers
- **Persevere** (15 XP) - Receive your first rejection
- **Resilient** (40 XP) - Get 5 rejections

### Diversity (3)

- **Wishlist Builder** (30 XP) - Add 10 wishlist items
- **Jack of All Trades** (35 XP) - Apply for 5 positions
- **Global Reach** (40 XP) - Apply to 5 locations

### Performance (3)

- **Quick Mover** (50 XP) - Get interview within 7 days
- **Century Club** (25 XP) - Accumulate 100 XP
- **Thousands** (100 XP) - Accumulate 1000 XP

## 📊 Database Models

### Application

```python
- id: Primary Key
- user: Foreign Key to User
- company: CharField (max 200)
- position: CharField (max 200)
- status: Choice (wishlist, applied, interview, offer, rejected)
- salary: CharField (optional)
- location: CharField (optional)
- notes: TextField (optional)
- created_at: DateTimeField (auto_now_add)
- updated_at: DateTimeField (auto_now)
```

### Achievement

```python
- id: Primary Key
- name: CharField (max 100, unique)
- description: TextField
- icon_class: CharField (Font Awesome class)
- color_class: CharField (Tailwind gradient)
- points: IntegerField
- criterion: CharField (unique trigger identifier)
- created_at: DateTimeField (auto_now_add)
```

### UserAchievement (M2M)

```python
- id: Primary Key
- user: Foreign Key to User
- achievement: Foreign Key to Achievement
- unlocked_at: DateTimeField (auto_now_add)
- Unique Constraint: (user, achievement)
```

### Milestone

```python
- id: Primary Key
- user: Foreign Key to User
- milestone_type: Choice (applications, offers, xp, achievements)
- title: CharField (max 200)
- description: TextField
- value: IntegerField
- achieved_at: DateTimeField (auto_now_add)
```

## 🔧 Configuration

### Django Settings

- **DEBUG**: True (development)
- **ALLOWED_HOSTS**: localhost, 127.0.0.1
- **DATABASE**: SQLite (db.sqlite3)
- **TIME_ZONE**: UTC

### Customization

Edit `resume/settings.py` to customize:

- Database settings
- Allowed hosts
- Static files configuration
- Email settings
- Theme settings

## 🌐 API Endpoints

### Authentication

- `GET /` - Home page
- `GET /login/` - Login page
- `POST /login/` - Login submission
- `GET /signup/` - Signup page
- `POST /signup/` - Signup submission
- `POST /logout/` - Logout

### Dashboard & Applications

- `GET /dashboard/` - Main dashboard
- `GET /add-application/` - Add application form
- `POST /add-application/` - Create application
- `POST /update-application-status/` - Update status (AJAX)

### User Profile

- `GET /profile/` - User profile
- `POST /profile/update-username/` - Update username
- `POST /profile/update-password/` - Update password

### Achievements

- `GET /achievements/` - View all achievements

### Leaderboard

- `GET /leaderboard/` - Global leaderboard
- `GET /leaderboard/milestones/` - Milestones page
- `GET /leaderboard/user/<user_id>/` - User detail page

## 🧪 Testing

### Manual Testing

1. Create a test account
2. Add 5+ applications
3. Change application statuses
4. Verify achievements unlock
5. Check milestones created
6. View leaderboard rankings

### Django Admin

```bash
python manage.py createsuperuser
python manage.py runserver
# Visit http://localhost:8000/admin
```

## 📝 Environment Variables

Create a `.env` file (optional):

```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🐛 Troubleshooting

### Achievements not unlocking

- Ensure `python manage.py initialize_achievements` was run
- Check database migrations: `python manage.py migrate`
- Verify Achievement model has data: `python manage.py shell`

### Tailwind CSS not applying

- Run `npm run build`
- Clear browser cache
- Restart development server

### Database errors

- Delete `db.sqlite3` and `*.pyc` files
- Run `python manage.py migrate --run-syncdb`
- Reinitialize achievements

## 📚 Documentation

For detailed documentation, see:

- [README_ACHIEVEMENTS.md](README_ACHIEVEMENTS.md) - Achievement system guide
- [ACHIEVEMENTS_GUIDE.md](ACHIEVEMENTS_GUIDE.md) - User guide for achievements
- [ACHIEVEMENT_SYSTEM_SUMMARY.md](ACHIEVEMENT_SYSTEM_SUMMARY.md) - Implementation details
- [ACHIEVEMENT_ARCHITECTURE.md](ACHIEVEMENT_ARCHITECTURE.md) - Technical architecture
- [LEADERBOARD_INTEGRATION.md](LEADERBOARD_INTEGRATION.md) - Leaderboard setup

## 🚀 Deployment

### Preparing for Production

1. **Update Django Settings**

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'your-production-secret-key'
```

2. **Collect Static Files**

```bash
python manage.py collectstatic --no-input
```

3. **Run Migrations**

```bash
python manage.py migrate
python manage.py initialize_achievements
```

### Hosting Options

- Heroku
- PythonAnywhere
- AWS
- DigitalOcean
- Railway

## 📜 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- Achievement progress indicators for in-progress achievements (future feature)
- Social sharing of achievements (future feature)
- Email notifications for milestones (future feature)

## 🎯 Future Features

- [ ] Achievement notifications/toasts
- [ ] Achievement streaks and combos
- [ ] Advanced analytics dashboard
- [ ] Social sharing integration
- [ ] Mobile app (React Native)
- [ ] Email notifications
- [ ] Interview preparation resources
- [ ] Job market insights
- [ ] Salary tracking and negotiation tools
- [ ] Resume builder integration

## 💡 Tips for Success

1. **Diverse Applications** - Apply to different positions and companies to unlock diversity achievements
2. **Consistent Effort** - Regular applications increase your chances of unlocking volume milestones
3. **Strategic Tracking** - Use notes to track why you moved applications through statuses
4. **Progress Monitoring** - Check the leaderboard to see how you compare to others
5. **Goal Setting** - Set milestones as goals to stay motivated

## 📞 Support

For issues, questions, or suggestions:

- Open an Issue on GitHub
- Check existing documentation
- Review achievement criteria in the app

## 👨‍💻 Author

Created as a comprehensive job search tracking application with gamification.

---

**Happy job hunting! 🚀**

Track your progress, earn achievements, and stay motivated on your path to your dream job!
