import uuid
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

class FreelancerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    profile_completeness = models.PositiveSmallIntegerField(default=0)
    profile_views = models.PositiveIntegerField(default=0)
    proposal_success_rate = models.PositiveSmallIntegerField(default=0)
    job_invitations = models.PositiveIntegerField(default=0)
    hourly_rate = models.PositiveIntegerField(default=0)
    skills = ArrayField(models.CharField(max_length=60), default=list, blank=True)
    portfolio_items = models.PositiveSmallIntegerField(default=0)
    repeat_clients_rate = models.PositiveSmallIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Profile of {self.user.email}'

class RoadmapMilestone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="roadmap_milestones")
    title = models.CharField(max_length=160)
    description = models.TextField()
    estimated_effort = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "order")
        ordering = ["order"]

    def __str__(self):
        return self.title

class RankingSnapshot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ranking_snapshots")
    value = models.PositiveSmallIntegerField()
    breakdown = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'Ranking for {self.user.email} at {self.created_at}'