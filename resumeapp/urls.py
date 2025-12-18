from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('achievements/', views.achievements_view, name='achievements'),
    path('add-application/', views.add_application, name='add_application'),
    path('update-application-status/', views.update_application_status, name='update_application_status'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update-username/', views.update_username, name='update_username'),
    path('profile/update-password/', views.update_password, name='update_password'),
]