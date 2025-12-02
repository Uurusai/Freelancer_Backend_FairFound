from rest_framework import serializers
from .models import FreelancerProfile, RoadmapMilestone, RankingSnapshot

class FreelancerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerProfile
        fields = [
            "user", "profile_completeness", "profile_views", "proposal_success_rate",
            "job_invitations", "hourly_rate", "skills", "portfolio_items",
            "repeat_clients_rate", "updated_at"
        ]

class RoadmapMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapMilestone
        fields = [
            "id", "user", "title", "description", "estimated_effort",
            "order", "completed", "created_at", "updated_at"
        ]

class RankingSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankingSnapshot
        fields = [
            "id", "user", "value", "breakdown", "created_at"
        ]