from django.urls import path
from .views import MyProfileView

urlpatterns = [
    path('me/profile/', MyProfileView.as_view()),
    # Add other endpoints as needed (ranking, roadmap, etc.)
]