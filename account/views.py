from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer

class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        user = get_object_or_404(User, pk=id)
        return Response(UserSerializer(user).data)

class UserSelfUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def patch(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserIndustryUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def patch(self, request):
        user = request.user
        industry = request.data.get("industry")
        if industry:
            user.industry = industry
            user.save()
            return Response({"industry": user.industry})
        return Response({"error": "Industry required"}, status=400)

class AuthMeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response(UserSerializer(request.user).data)