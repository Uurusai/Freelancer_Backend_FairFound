from rest_framework import serializers
from .models import SentimentReview

class SentimentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentimentReview
        fields = [
            "id", "user", "text", "score", "label", "categories", "suggestions", "created_at"
        ]