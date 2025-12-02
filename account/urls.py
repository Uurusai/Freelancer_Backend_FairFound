from django.urls import path
from .views import UserDetailView, UserSelfUpdateView, UserIndustryUpdateView, AuthMeView

urlpatterns = [
    path("me/", UserSelfUpdateView.as_view()),
    path("me/industry/", UserIndustryUpdateView.as_view()),
    path("<uuid:id>/", UserDetailView.as_view()),
    path("me/info/", AuthMeView.as_view()),
]