import uuid
from django.db import models
from django.conf import settings

class ComparisonEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comparisons")
    competitor_identifier = models.CharField(max_length=160)
    competitor_role = models.CharField(max_length=80)
    pseudo_ranking = models.PositiveSmallIntegerField()
    snapshot = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]