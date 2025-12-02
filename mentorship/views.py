from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import MentorshipRequest, MentorshipMessage
from .serializers import MentorshipRequestSerializer, MentorshipMessageSerializer
from django.shortcuts import get_object_or_404

class MentorshipRequestViewSet(ModelViewSet):
    serializer_class = MentorshipRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        mine = self.request.query_params.get("mine")
        if mine == "true":
            return MentorshipRequest.objects.filter(requester=user)
        status_param = self.request.query_params.get("status")
        qs = MentorshipRequest.objects.all()
        if status_param:
            qs = qs.filter(status=status_param)
        return qs
    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

class MentorshipRequestDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        req = get_object_or_404(MentorshipRequest, pk=pk)
        return Response(MentorshipRequestSerializer(req).data)
    def patch(self, request, pk):
        req = get_object_or_404(MentorshipRequest, pk=pk)
        serializer = MentorshipRequestSerializer(req, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class MentorshipMessageViewSet(ModelViewSet):
    serializer_class = MentorshipMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        request_id = self.kwargs.get("request_pk")
        return MentorshipMessage.objects.filter(request_id=request_id)
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class MentorDashboardRequestsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        qs = MentorshipRequest.objects.filter(mentor=request.user)
        status_param = request.GET.get("status")
        if status_param:
            qs = qs.filter(status=status_param)
        return Response(MentorshipRequestSerializer(qs, many=True).data)