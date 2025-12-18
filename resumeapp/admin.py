from django.contrib import admin
from .models import Application, Achievement, UserAchievement


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'status', 'work_setup', 'source', 'salary', 'created_at')
    list_filter = ('status', 'work_setup', 'source', 'created_at')
    search_fields = ('company', 'position', 'location')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Job Details', {
            'fields': ('user', 'company', 'position', 'location', 'salary')
        }),
        ('Application Info', {
            'fields': ('status', 'work_setup', 'source')
        }),
        ('Additional', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'criterion', 'points', 'color_class')
    list_filter = ('criterion',)
    search_fields = ('name', 'description')


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'unlocked_at')
    list_filter = ('unlocked_at', 'achievement')
    search_fields = ('user__username', 'achievement__name')
    readonly_fields = ('unlocked_at',)
