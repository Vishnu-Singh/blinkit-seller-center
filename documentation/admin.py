from django.contrib import admin
from .models import APIEndpoint, Changelog, SetupStep


@admin.register(APIEndpoint)
class APIEndpointAdmin(admin.ModelAdmin):
    """Admin interface for API Endpoint documentation."""
    
    list_display = ('name', 'app_name', 'protocol', 'method', 'path', 'is_active', 'updated_at')
    list_filter = ('protocol', 'method', 'app_name', 'is_active')
    search_fields = ('name', 'path', 'description')
    ordering = ('app_name', 'protocol', 'path')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'app_name', 'protocol', 'method', 'path', 'description', 'is_active')
        }),
        ('Examples', {
            'fields': ('request_example', 'response_example', 'parameters')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Changelog)
class ChangelogAdmin(admin.ModelAdmin):
    """Admin interface for Changelog."""
    
    list_display = ('version', 'change_type', 'title', 'app_affected', 'release_date')
    list_filter = ('change_type', 'release_date', 'app_affected')
    search_fields = ('title', 'description', 'version')
    ordering = ('-release_date', '-created_at')
    date_hierarchy = 'release_date'
    
    fieldsets = (
        ('Version Information', {
            'fields': ('version', 'release_date')
        }),
        ('Change Details', {
            'fields': ('change_type', 'title', 'description', 'app_affected')
        }),
    )


@admin.register(SetupStep)
class SetupStepAdmin(admin.ModelAdmin):
    """Admin interface for Setup Steps."""
    
    list_display = ('order', 'title', 'is_required', 'created_at')
    list_filter = ('is_required',)
    search_fields = ('title', 'description', 'command')
    ordering = ('order',)
    
    fieldsets = (
        ('Step Information', {
            'fields': ('order', 'title', 'is_required')
        }),
        ('Instructions', {
            'fields': ('description', 'command')
        }),
    )
