from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComparisonEntryViewSet, ComparisonEntryBulkDelete

router = DefaultRouter()
router.register(r"me/comparisons", ComparisonEntryViewSet, basename="comparisons")

urlpatterns = [
    path("me/comparisons/", ComparisonEntryBulkDelete.as_view()),  # DELETE bulk
    path("", include(router.urls)),
]