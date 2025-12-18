from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserStats, Milestone
from resumeapp.models import Application, UserAchievement


def leaderboard_view(request):
    """Display the global leaderboard with rankings"""
    
    # Get all user stats ordered by XP (descending)
    leaderboard_entries = UserStats.objects.all().order_by('-total_xp')
    
    # Add rank to each entry
    ranked_entries = []
    for rank, entry in enumerate(leaderboard_entries, 1):
        ranked_entries.append({
            'rank': rank,
            'user_stats': entry,
            'is_current_user': request.user.is_authenticated and entry.user == request.user
        })
    
    # Get current user's stats if authenticated
    current_user_stats = None
    current_user_rank = None
    if request.user.is_authenticated:
        try:
            current_user_stats = UserStats.objects.get(user=request.user)
            current_user_rank = next(
                (entry['rank'] for entry in ranked_entries if entry['user_stats'].id == current_user_stats.id),
                None
            )
        except UserStats.DoesNotExist:
            pass
    
    context = {
        'leaderboard_entries': ranked_entries[:50],  # Top 50
        'current_user_stats': current_user_stats,
        'current_user_rank': current_user_rank,
        'total_users': leaderboard_entries.count(),
        'filter_type': 'xp',
    }
    
    return render(request, 'leaderboard_main.html', context)


@login_required(login_url='login')
def leaderboard_detail_view(request, username):
    """Display detailed stats for a specific user"""
    try:
        user = User.objects.get(username=username)
        user_stats = UserStats.objects.get(user=user)
        applications = Application.objects.filter(user=user)
        milestones = Milestone.objects.filter(user=user)[:10]
        
        # Calculate user rank
        rank = UserStats.objects.filter(total_xp__gt=user_stats.total_xp).count() + 1
        
        # Calculate stats breakdown
        status_breakdown = {
            'wishlist': applications.filter(status='wishlist').count(),
            'applied': applications.filter(status='applied').count(),
            'interview': applications.filter(status='interview').count(),
            'offer': applications.filter(status='offer').count(),
            'rejected': applications.filter(status='rejected').count(),
        }
        
        context = {
            'profile_user': user,
            'user_stats': user_stats,
            'rank': rank,
            'total_users': UserStats.objects.count(),
            'applications': applications[:10],  # Recent apps
            'milestones': milestones,
            'status_breakdown': status_breakdown,
            'is_own_profile': request.user == user,
        }
        
        return render(request, 'user_detail.html', context)
    except (User.DoesNotExist, UserStats.DoesNotExist):
        context = {'error': 'User not found'}
        return render(request, 'user_detail.html', context, status=404)


@login_required(login_url='login')
def milestones_view(request):
    """Display user's milestones"""
    user_milestones = Milestone.objects.filter(user=request.user)
    
    # Group milestones by type
    milestone_groups = {}
    for milestone_type, milestone_label in Milestone.MILESTONE_TYPES:
        milestone_groups[milestone_type] = {
            'label': milestone_label,
            'milestones': user_milestones.filter(milestone_type=milestone_type)
        }
    
    context = {
        'milestone_groups': milestone_groups,
        'total_milestones': user_milestones.count(),
    }
    
    return render(request, 'milestones.html', context)


def stats_by_filter_view(request, filter_type):
    """Display leaderboard filtered by specific stat"""
    
    if filter_type == 'xp':
        leaderboard_entries = UserStats.objects.all().order_by('-total_xp')
        title = "Top Users by XP"
        metric = "XP"
    elif filter_type == 'applications':
        leaderboard_entries = UserStats.objects.all().order_by('-total_applications')
        title = "Top Users by Applications"
        metric = "Applications"
    elif filter_type == 'offers':
        leaderboard_entries = UserStats.objects.all().order_by('-total_offers')
        title = "Top Users by Offers"
        metric = "Offers"
    elif filter_type == 'achievements':
        leaderboard_entries = UserStats.objects.all().order_by('-total_achievements')
        title = "Top Users by Achievements"
        metric = "Achievements"
    else:
        leaderboard_entries = UserStats.objects.all().order_by('-total_xp')
        title = "Leaderboard"
        metric = "XP"
    
    # Add rank to each entry
    ranked_entries = []
    for rank, entry in enumerate(leaderboard_entries, 1):
        ranked_entries.append({
            'rank': rank,
            'user_stats': entry,
            'is_current_user': request.user.is_authenticated and entry.user == request.user
        })
    
    # Get current user's stats if authenticated
    current_user_stats = None
    current_user_rank = None
    if request.user.is_authenticated:
        try:
            current_user_stats = UserStats.objects.get(user=request.user)
            current_user_rank = next(
                (entry['rank'] for entry in ranked_entries if entry['user_stats'].id == current_user_stats.id),
                None
            )
        except UserStats.DoesNotExist:
            pass
    
    context = {
        'leaderboard_entries': ranked_entries[:50],
        'title': title,
        'metric': metric,
        'filter_type': filter_type,
        'total_users': leaderboard_entries.count(),
        'current_user_stats': current_user_stats,
        'current_user_rank': current_user_rank,
    }
    
    return render(request, 'leaderboard_main.html', context)
