from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FreelancerProfile, RoadmapMilestone, RankingSnapshot
from .serializers import (
    FreelancerProfileSerializer,
    RoadmapMilestoneSerializer,
    RankingSnapshotSerializer,
)
from django.shortcuts import get_object_or_404

class MyProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        profile, _ = FreelancerProfile.objects.get_or_create(user=request.user)
        serializer = FreelancerProfileSerializer(profile)
        return Response(serializer.data)

    def patch(self, request):
        profile, _ = FreelancerProfile.objects.get_or_create(user=request.user)
        serializer = FreelancerProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RoadmapMilestoneViewSet(viewsets.ModelViewSet):
    serializer_class = RoadmapMilestoneSerializer

    def get_queryset(self):
        return RoadmapMilestone.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)