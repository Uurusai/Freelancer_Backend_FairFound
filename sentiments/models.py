import uuid
from django.db import models
from django.conf import settings

class SentimentReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sentiment_reviews")
    text = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    label = models.CharField(max_length=10, choices=[("positive","positive"),("neutral","neutral"),("negative","negative")])
    categories = models.JSONField(default=list)
    suggestions = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)