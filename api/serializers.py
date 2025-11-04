"""Serializers for API models."""
from rest_framework import serializers
from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'id',
            'session_id',
            'patient_id',
            'status',
            'current_step',
            'total_steps',
            'started_at',
            'completed_at',
            'metadata',
        ]
        read_only_fields = ['id', 'started_at']


class SessionCreateSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length=100)
    patient_id = serializers.CharField(max_length=100, required=False, allow_blank=True)
    total_steps = serializers.IntegerField(default=4)
    metadata = serializers.JSONField(required=False, default=dict)


class SessionUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(
        choices=['started', 'in_progress', 'completed', 'failed'],
        required=False
    )
    current_step = serializers.IntegerField(required=False)
    metadata = serializers.JSONField(required=False)
