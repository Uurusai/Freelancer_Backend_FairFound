from rest_framework import serializers
from .models import ComparisonEntry

class ComparisonEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisonEntry
        fields = [
            "id", "user", "competitor_identifier", "competitor_role", "pseudo_ranking", "snapshot", "created_at"
        ]