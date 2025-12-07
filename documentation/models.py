from django.db import models


class APIEndpoint(models.Model):
    """Model to store API endpoint documentation."""
    
    PROTOCOL_CHOICES = [
        ('REST', 'REST API'),
        ('SOAP', 'SOAP API'),
    ]
    
    METHOD_CHOICES = [
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE'),
        ('SOAP', 'SOAP Operation'),
    ]
    
    name = models.CharField(max_length=255, help_text="Endpoint name")
    app_name = models.CharField(max_length=100, help_text="Django app name")
    protocol = models.CharField(max_length=10, choices=PROTOCOL_CHOICES)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    path = models.CharField(max_length=500, help_text="API path")
    description = models.TextField()
    request_example = models.TextField(blank=True, help_text="Example request body")
    response_example = models.TextField(blank=True, help_text="Example response")
    parameters = models.TextField(blank=True, help_text="Query parameters or path parameters")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['app_name', 'protocol', 'path']
    
    def __str__(self):
        return f"{self.protocol} - {self.method} {self.path}"


class Changelog(models.Model):
    """Model to track changes and versions."""
    
    CHANGE_TYPE_CHOICES = [
        ('feature', 'New Feature'),
        ('enhancement', 'Enhancement'),
        ('bugfix', 'Bug Fix'),
        ('breaking', 'Breaking Change'),
        ('documentation', 'Documentation'),
    ]
    
    version = models.CharField(max_length=50, help_text="Version number (e.g., 1.0.0)")
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    app_affected = models.CharField(max_length=100, blank=True, help_text="App affected by this change")
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-release_date', '-created_at']
    
    def __str__(self):
        return f"v{self.version} - {self.title}"


class SetupStep(models.Model):
    """Model to store setup instructions."""
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    command = models.TextField(blank=True, help_text="Command to execute")
    order = models.IntegerField(default=0, help_text="Display order")
    is_required = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.order}. {self.title}"
