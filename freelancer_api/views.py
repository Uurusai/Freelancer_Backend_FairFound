from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import UserProfile, ProfileComparison, SWOTAnalysis, CareerRoadmap, Skill
from .serializers import (
    UserProfileSerializer, ProfileComparisonSerializer,
    SWOTAnalysisSerializer, CareerRoadmapSerializer, SkillSerializer
)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileComparisonViewSet(viewsets.ModelViewSet):
    queryset = ProfileComparison.objects.all()
    serializer_class = ProfileComparisonSerializer
    
    @action(detail=False, methods=['post'])
    def compare(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        compare_with_id = request.data.get('compare_with')
        
        if not compare_with_id:
            return Response(
                {'error': 'compare_with field is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        compare_with = get_object_or_404(UserProfile, id=compare_with_id)
        
        # Calculate comparison score (simplified example)
        comparison_score = self.calculate_comparison_score(user_profile, compare_with)
        
        comparison, created = ProfileComparison.objects.get_or_create(
            user_profile=user_profile,
            compare_with=compare_with,
            defaults={'comparison_score': comparison_score}
        )
        
        if not created:
            comparison.comparison_score = comparison_score
            comparison.save()
        
        serializer = self.get_serializer(comparison)
        return Response(serializer.data)
    
    def calculate_comparison_score(self, profile1, profile2):
        score = 0
        common_skills = profile1.skills.filter(id__in=profile2.skills.all())
        score += common_skills.count() * 10
        
        if profile1.rating and profile2.rating:
            score += int((profile1.rating - profile2.rating) * 20)
        
        return score

class SWOTAnalysisViewSet(viewsets.ModelViewSet):
    queryset = SWOTAnalysis.objects.all()
    serializer_class = SWOTAnalysisSerializer
    
    @action(detail=False, methods=['post'])
    def generate_swot(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)

        swot_analysis, created = SWOTAnalysis.objects.get_or_create(
            user_profile=user_profile,
            defaults=self.generate_swot_content(user_profile)
        )
        
        serializer = self.get_serializer(swot_analysis)
        return Response(serializer.data)
    
    def generate_swot_content(self, user_profile):

        return {
            'strengths': f"Strong skills in {', '.join(skill.name for skill in user_profile.skills.all()[:3])}",
            'weaknesses': "Limited portfolio items" if not user_profile.portfolio else "Good portfolio",
            'opportunities': "High demand for your skills in current market",
            'threats': "Increasing competition in your field"
        }

class CareerRoadmapViewSet(viewsets.ModelViewSet):
    queryset = CareerRoadmap.objects.all()
    serializer_class = CareerRoadmapSerializer
    
    @action(detail=False, methods=['post'])
    def generate_roadmap(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        
        roadmap, created = CareerRoadmap.objects.get_or_create(
            user_profile=user_profile,
            defaults={
                'steps': self.generate_roadmap_steps(user_profile),
                'visibility_boost': False
            }
        )
        
        serializer = self.get_serializer(roadmap)
        return Response(serializer.data)
    
    def generate_roadmap_steps(self, user_profile):
        steps = [
            "Complete your profile with detailed bio",
            "Add at least 5 portfolio items",
            "Acquire 2 new relevant skills",
            "Get your first client review",
            "Increase your pricing by 20% after 5 successful projects"
        ]
        return "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps))

class RankingViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def get_rank(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        
        rank_score = self.calculate_pseudo_rank(user_profile)
        
        return Response({
            'user_profile_id': user_profile.id,
            'pseudo_rank': rank_score,
            'message': 'Rank calculated successfully'
        })
    
    def calculate_pseudo_rank(self, user_profile):
        score = 0
        if user_profile.bio:
            score += 20
        if user_profile.portfolio:
            score += 20
        if user_profile.pricing:
            score += 20
        if user_profile.skills.exists():
            score += min(user_profile.skills.count() * 5, 20)
        if user_profile.rating:
            score += 20
        
        return score