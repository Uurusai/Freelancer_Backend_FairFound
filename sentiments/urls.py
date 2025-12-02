from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SentimentReviewViewSet,
    SentimentAggregateView,
    SentimentExportView,
    SentimentBulkDelete,
)

router = DefaultRouter()
router.register(r"me/feedback", SentimentReviewViewSet, basename="feedback")

urlpatterns = [
    path("me/feedback/aggregate/", SentimentAggregateView.as_view()),
    path("me/feedback/export/", SentimentExportView.as_view()),
    path("me/feedback/", SentimentBulkDelete.as_view()),  # DELETE all feedback
    path("", include(router.urls)),
]