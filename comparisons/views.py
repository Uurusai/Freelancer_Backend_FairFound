from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import ComparisonEntry
from .serializers import ComparisonEntrySerializer

class ComparisonEntryViewSet(ModelViewSet):
    serializer_class = ComparisonEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        role = self.request.query_params.get("role")
        qs = ComparisonEntry.objects.filter(user=user)
        if role:
            qs = qs.filter(competitor_role=role)
        return qs
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ComparisonEntryBulkDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request):
        ComparisonEntry.objects.filter(user=request.user).delete()
        return Response({"deleted": True})
