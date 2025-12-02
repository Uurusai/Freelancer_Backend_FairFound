from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MentorshipRequestViewSet,
    MentorshipRequestDetailView,
    MentorshipMessageViewSet,
    MentorDashboardRequestsView,
)

router = DefaultRouter()
router.register(r"requests", MentorshipRequestViewSet, basename="requests")

urlpatterns = [
    path("requests/<uuid:pk>/", MentorshipRequestDetailView.as_view()),                # GET/PATCH
    path("dashboard/requests/", MentorDashboardRequestsView.as_view()),                # Mentor dashboard
    path("requests/<uuid:request_pk>/messages/", MentorshipMessageViewSet.as_view({"get":"list","post":"create"})), # messages
    path("", include(router.urls)),
]