
from django.urls import path
from .views import UserDetailView, UserSelfUpdateView, UserIndustryUpdateView, AuthMeView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("me/", UserSelfUpdateView.as_view()),
    path("me/industry/", UserIndustryUpdateView.as_view()),
    path("<uuid:id>/", UserDetailView.as_view()),
    path("me/info/", AuthMeView.as_view()),
]