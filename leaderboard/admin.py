from django.contrib import admin
from .models import UserStats, Milestone


@admin.register(UserStats)
class UserStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'total_xp', 'total_applications', 'total_offers', 'last_updated')
    list_filter = ('level', 'last_updated')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('last_updated',)
    ordering = ('-total_xp',)


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'milestone_type', 'value', 'achieved_at')
    list_filter = ('milestone_type', 'achieved_at')
    search_fields = ('user__username', 'title')
    ordering = ('-achieved_at',)
