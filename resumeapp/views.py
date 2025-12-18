from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Application, Achievement, UserAchievement

# Achievement unlocking utility function
def check_and_unlock_achievement(user, criterion):
    """Check if user should unlock an achievement based on criterion"""
    try:
        achievement = Achievement.objects.get(criterion=criterion)
        
        # Check if already unlocked
        if UserAchievement.objects.filter(user=user, achievement=achievement).exists():
            return False
        
        # Unlock the achievement
        UserAchievement.objects.create(user=user, achievement=achievement)
        return True
    except Achievement.DoesNotExist:
        return False

def check_all_achievements(user):
    """Check all achievement criteria for a user"""
    applications = Application.objects.filter(user=user)
    
    # First Application
    if applications.count() == 1:
        check_and_unlock_achievement(user, 'first_application')
    
    # Five Applications
    elif applications.count() == 5:
        check_and_unlock_achievement(user, 'five_applications')
    
    # Ten Applications
    elif applications.count() == 10:
        check_and_unlock_achievement(user, 'ten_applications')
    
    # Twenty Five Applications
    elif applications.count() == 25:
        check_and_unlock_achievement(user, 'twenty_five_applications')
    
    # First Applied
    if applications.filter(status='applied').exists() and not UserAchievement.objects.filter(user=user, achievement__criterion='first_applied').exists():
        check_and_unlock_achievement(user, 'first_applied')
    
    # First Interview
    if applications.filter(status='interview').exists() and not UserAchievement.objects.filter(user=user, achievement__criterion='first_interview').exists():
        check_and_unlock_achievement(user, 'first_interview')
    
    # Five Interviews
    interview_count = applications.filter(status='interview').count()
    if interview_count >= 5 and not UserAchievement.objects.filter(user=user, achievement__criterion='five_interviews').exists():
        check_and_unlock_achievement(user, 'five_interviews')
    
    # First Offer
    if applications.filter(status='offer').exists() and not UserAchievement.objects.filter(user=user, achievement__criterion='first_offer').exists():
        check_and_unlock_achievement(user, 'first_offer')
    
    # Three Offers
    offer_count = applications.filter(status='offer').count()
    if offer_count >= 3 and not UserAchievement.objects.filter(user=user, achievement__criterion='three_offers').exists():
        check_and_unlock_achievement(user, 'three_offers')
    
    # First Rejection
    if applications.filter(status='rejected').exists() and not UserAchievement.objects.filter(user=user, achievement__criterion='first_rejection').exists():
        check_and_unlock_achievement(user, 'first_rejection')
    
    # Five Rejections
    rejection_count = applications.filter(status='rejected').count()
    if rejection_count >= 5 and not UserAchievement.objects.filter(user=user, achievement__criterion='five_rejections').exists():
        check_and_unlock_achievement(user, 'five_rejections')
    
    # Ten Wishlist
    wishlist_count = applications.filter(status='wishlist').count()
    if wishlist_count >= 10 and not UserAchievement.objects.filter(user=user, achievement__criterion='ten_wishlist').exists():
        check_and_unlock_achievement(user, 'ten_wishlist')
    
    # Five Different Positions
    unique_positions = applications.values('position').distinct().count()
    if unique_positions >= 5 and not UserAchievement.objects.filter(user=user, achievement__criterion='five_positions').exists():
        check_and_unlock_achievement(user, 'five_positions')
    
    # Five Different Locations
    unique_locations = applications.exclude(location='').values('location').distinct().count()
    if unique_locations >= 5 and not UserAchievement.objects.filter(user=user, achievement__criterion='five_locations').exists():
        check_and_unlock_achievement(user, 'five_locations')
    
    # Quick Mover (moved to interview within 7 days)
    seven_days_ago = timezone.now() - timedelta(days=7)
    quick_interviews = applications.filter(status='interview', created_at__gte=seven_days_ago).count()
    if quick_interviews > 0 and not UserAchievement.objects.filter(user=user, achievement__criterion='quick_interview').exists():
        check_and_unlock_achievement(user, 'quick_interview')
    
    # XP Achievements
    total_xp = sum(app.get_xp() for app in applications)
    if total_xp >= 100 and not UserAchievement.objects.filter(user=user, achievement__criterion='hundred_xp').exists():
        check_and_unlock_achievement(user, 'hundred_xp')
    
    if total_xp >= 1000 and not UserAchievement.objects.filter(user=user, achievement__criterion='thousand_xp').exists():
        check_and_unlock_achievement(user, 'thousand_xp')

# views.py example
def home(request):
    return render(request, 'index.html')

def signup_view(request):
    # Handle signup logic here
    return render(request, 'signup.html')

def login_view(request):
    # Handle login logic here
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation checks
        if not full_name or not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required!")
            return redirect('signup')
        
        if len(username) < 3:
            messages.error(request, "Username must be at least 3 characters long!")
            return redirect('signup')
        
        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long!")
            return redirect('signup')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken. Please choose a different one.")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered. Please use a different email or login.")
            return redirect('signup')
            
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = full_name
            user.save()
            
            messages.success(request, "Account created successfully! Redirecting to your dashboard...")
            login(request, user)
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('signup')
        
    return render(request, 'signup.html')

@login_required(login_url='login')
def achievements_view(request):
    # Get all achievements
    all_achievements = Achievement.objects.all()
    
    # Get user's unlocked achievements with unlock dates
    user_achievements = UserAchievement.objects.filter(user=request.user)
    unlocked_achievement_ids = {ua.achievement_id: ua for ua in user_achievements}
    
    # Build achievement list with unlocked status and date
    achievements_data = []
    for achievement in all_achievements:
        user_achievement = unlocked_achievement_ids.get(achievement.id)
        achievements_data.append({
            'achievement': achievement,
            'unlocked': user_achievement is not None,
            'unlocked_date': user_achievement.unlocked_at if user_achievement else None,
        })
    
    unlocked_count = len(user_achievements)
    total_count = all_achievements.count()
    completion_percentage = int((unlocked_count / total_count * 100) if total_count > 0 else 0)
    
    # Calculate total points from unlocked achievements
    total_points = sum(achievement.points for achievement in [ua.achievement for ua in user_achievements])
    
    context = {
        'achievements': achievements_data,
        'unlocked_count': unlocked_count,
        'total_count': total_count,
        'completion_percentage': completion_percentage,
        'total_points': total_points,
    }
    return render(request, 'achievements.html', context)

@login_required(login_url='login')
def dashboard_view(request):
    # Ensure only logged in users see this
    applications = Application.objects.filter(user=request.user)
    
    # Group applications by status
    kanban_data = {
        'wishlist': applications.filter(status='wishlist'),
        'applied': applications.filter(status='applied'),
        'interview': applications.filter(status='interview'),
        'offer': applications.filter(status='offer'),
        'rejected': applications.filter(status='rejected'),
    }
    
    # Get all achievements
    all_achievements = Achievement.objects.all()
    
    # Get user's unlocked achievements with unlock dates
    user_achievements = UserAchievement.objects.filter(user=request.user)
    unlocked_achievement_ids = {ua.achievement_id: ua for ua in user_achievements}
    
    # Build achievement list with unlocked status and date
    achievements_data = []
    for achievement in all_achievements:
        user_achievement = unlocked_achievement_ids.get(achievement.id)
        achievements_data.append({
            'achievement': achievement,
            'unlocked': user_achievement is not None,
            'unlocked_date': user_achievement.unlocked_at if user_achievement else None,
        })
    
    unlocked_count = len(user_achievements)
    total_count = all_achievements.count()
    completion_percentage = int((unlocked_count / total_count * 100) if total_count > 0 else 0)
    
    # Get recent milestones
    from leaderboard.models import Milestone
    recent_milestones = Milestone.objects.filter(user=request.user).order_by('-achieved_at')[:5]
    
    context = {
        'applications': applications,
        'kanban_data': kanban_data,
        'status_counts': {
            'applied': applications.filter(status='applied').count(),
            'interview': applications.filter(status='interview').count(),
            'offer': applications.filter(status='offer').count(),
            'rejected': applications.filter(status='rejected').count(),
        },
        'achievements': achievements_data,
        'unlocked_count': unlocked_count,
        'total_count': total_count,
        'completion_percentage': completion_percentage,
        'recent_milestones': recent_milestones,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def add_application(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        position = request.POST.get('position')
        status = request.POST.get('status', 'wishlist')
        salary = request.POST.get('salary', '')
        location = request.POST.get('location', '')
        notes = request.POST.get('notes', '')
        
        app = Application.objects.create(
            user=request.user,
            company=company,
            position=position,
            status=status,
            salary=salary,
            location=location,
            notes=notes
        )
        
        # Check and unlock achievements
        check_all_achievements(request.user)
        
        messages.success(request, f"Application added for {position} at {company}!")
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'redirect': '/dashboard/'})
        return redirect('dashboard')
    
    return render(request, 'add_application_modal.html')

@login_required(login_url='login')
def profile_view(request):
    """Display user profile"""
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def update_username(request):
    """Update username"""
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        
        if not new_username:
            messages.error(request, "Username cannot be empty!")
            return redirect('profile')
        
        if User.objects.filter(username=new_username).exclude(id=request.user.id).exists():
            messages.error(request, "This username is already taken!")
            return redirect('profile')
        
        try:
            request.user.username = new_username
            request.user.save()
            messages.success(request, f"Username updated to {new_username}!")
            return redirect('profile')
        except Exception as e:
            messages.error(request, f"Error updating username: {str(e)}")
            return redirect('profile')
    
    return redirect('profile')

@login_required(login_url='login')
def update_password(request):
    """Update password"""
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not request.user.check_password(current_password):
            messages.error(request, "Current password is incorrect!")
            return redirect('profile')
        
        if new_password != confirm_password:
            messages.error(request, "New passwords do not match!")
            return redirect('profile')
        
        if len(new_password) < 6:
            messages.error(request, "Password must be at least 6 characters long!")
            return redirect('profile')
        
        try:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Password updated successfully!")
            return redirect('profile')
        except Exception as e:
            messages.error(request, f"Error updating password: {str(e)}")
            return redirect('profile')
    
    return redirect('profile')

@login_required(login_url='login')
def update_application_status(request):
    """AJAX endpoint to update application status via drag and drop"""
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            app_id = data.get('app_id')
            new_status = data.get('status')
            
            app = Application.objects.get(id=app_id, user=request.user)
            app.status = new_status
            app.save()
            
            # Check and unlock achievements
            check_all_achievements(request.user)
            
            return JsonResponse({
                'success': True,
                'message': f'Application moved to {new_status}',
                'xp': app.get_xp()
            })
        except Application.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Application not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)