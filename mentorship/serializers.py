from rest_framework import serializers
from .models import MentorshipRequest, MentorshipMessage

class MentorshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipRequest
        fields = [
            "id", "topic", "context", "preferred_expertise", "status",
            "requester", "mentor", "created_at", "updated_at"
        ]

class MentorshipMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipMessage
        fields = [
            "id", "request", "sender", "text", "created_at"
        ]