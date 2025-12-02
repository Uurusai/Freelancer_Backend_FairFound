from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Skill, ProfileComparison, SWOTAnalysis, CareerRoadmap

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class UserProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    skill_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'email', 'skills', 'skill_ids', 
            'portfolio', 'bio', 'pricing', 'pseudo_rank', 'rating'
        ]
    
    def create(self, validated_data):
        skill_ids = validated_data.pop('skill_ids', [])
        profile = UserProfile.objects.create(**validated_data)
        profile.skills.set(skill_ids)
        return profile
    
    def update(self, instance, validated_data):
        skill_ids = validated_data.pop('skill_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if skill_ids is not None:
            instance.skills.set(skill_ids)
        
        return instance

class ProfileComparisonSerializer(serializers.ModelSerializer):
    user_profile_name = serializers.CharField(source='user_profile.user.username', read_only=True)
    compare_with_name = serializers.CharField(source='compare_with.user.username', read_only=True)
    
    class Meta:
        model = ProfileComparison
        fields = ['id', 'user_profile', 'user_profile_name', 'compare_with', 
                 'compare_with_name', 'comparison_score', 'created_at']

class SWOTAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWOTAnalysis
        fields = ['id', 'user_profile', 'strengths', 'weaknesses', 
                 'opportunities', 'threats', 'created_at', 'updated_at']

class CareerRoadmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerRoadmap
        fields = ['id', 'user_profile', 'steps', 'visibility_boost', 
                 'created_at', 'updated_at']