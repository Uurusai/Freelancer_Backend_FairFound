from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    skills = models.ManyToManyField(Skill, blank=True)
    portfolio = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True)
    pricing = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pseudo_rank = models.IntegerField(default=0)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class ProfileComparison(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comparisons_made')
    compare_with = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='compared_by_others')
    comparison_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user_profile', 'compare_with']
    
    def __str__(self):
        return f"{self.user_profile.user.username} vs {self.compare_with.user.username}"

class SWOTAnalysis(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='swot_analysis')
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    opportunities = models.TextField(blank=True)
    threats = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"SWOT Analysis for {self.user_profile.user.username}"

class CareerRoadmap(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='career_roadmap')
    steps = models.TextField(help_text="JSON string or text describing career steps")
    visibility_boost = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Career Roadmap for {self.user_profile.user.username}"