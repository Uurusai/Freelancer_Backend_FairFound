from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Industry
from .serializers import IndustrySerializer
from django.shortcuts import get_object_or_404

class IndustryListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response(IndustrySerializer(Industry.objects.all(), many=True).data)

class IndustryDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, slug):
        inds = get_object_or_404(Industry, slug=slug)
        return Response(IndustrySerializer(inds).data)