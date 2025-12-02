from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer
from rest_framework import status

class RegisterView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                name=serializer.validated_data['name'],
                password=request.data['password']
            )
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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