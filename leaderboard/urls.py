from django.urls import path
from . import views

app_name = 'leaderboard'

urlpatterns = [
    path('', views.leaderboard_view, name='leaderboard'),
    path('user/<str:username>/', views.leaderboard_detail_view, name='user_detail'),
    path('milestones/', views.milestones_view, name='milestones'),
    path('stats/<str:filter_type>/', views.stats_by_filter_view, name='stats_filtered'),
]
