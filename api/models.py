"""Models for the Medichek API."""
from django.db import models
from django.utils import timezone


class Session(models.Model):
    """Represents a patient medication application session."""
    
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    session_id = models.CharField(max_length=100, unique=True, db_index=True)
    patient_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='started')
    current_step = models.IntegerField(default=0)
    total_steps = models.IntegerField(default=4)
    
    started_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    metadata = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ['-started_at']
    
    def __str__(self):
        return f"Session {self.session_id} - {self.status}"
