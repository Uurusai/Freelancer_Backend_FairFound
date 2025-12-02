from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import datetime

class HealthView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"status": "ok", "time": datetime.datetime.utcnow().isoformat()})

class SuggestionsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        role = request.GET.get("role")
        limit = int(request.GET.get("limit", 5))
        # Dummy competitors
        data = []
        for i in range(limit):
            data.append({
                "role": role or "freelancer",
                "identifier": f"competitor_{i}",
                "hourly_rate": 45 + i*2,
                "portfolio_items": 8 + i,
                "pseudo_ranking": 50 + i*5
            })
        return Response(data)