from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import SentimentReview
from .serializers import SentimentReviewSerializer
from django.shortcuts import get_object_or_404
#from core.services import aggregate_reviews, analyze_text  # As spec

class SentimentReviewViewSet(ModelViewSet):
    serializer_class = SentimentReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return SentimentReview.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        data = serializer.validated_data
        if not ("score" in data and "label" in data):
            #need to define analyze_text function in core.services
            analysis = {"score": 0, "label": "neutral", "categories": [], "suggestions": []}
            #analysis = analyze_text(data["text"])
            serializer.save(user=self.request.user, **analysis)
        else:
            serializer.save(user=self.request.user)

class SentimentAggregateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        
        #result = aggregate_reviews(request.user)
        result = {
            "total_reviews": SentimentReview.objects.filter(user=request.user).count(),
            "average_score": SentimentReview.objects.filter(user=request.user).aggregate_avg('score'),
            "label_distribution": {
                "positive": SentimentReview.objects.filter(user=request.user, label="positive").count(),
                "neutral": SentimentReview.objects.filter(user=request.user, label="neutral").count(),
                "negative": SentimentReview.objects.filter(user=request.user, label="negative").count(),
            }
        } #placeholder for actual aggregation logic
        return Response(result)

class SentimentExportView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        import csv, io
        if request.GET.get("format") == "csv":
            reviews = SentimentReview.objects.filter(user=request.user)
            buf = io.StringIO()
            writer = csv.writer(buf)
            writer.writerow(["id", "text", "score", "label", "categories", "suggestions", "created_at"])
            for r in reviews:
                writer.writerow([
                    r.id, r.text, r.score, r.label, ",".join(r.categories), ",".join(r.suggestions), r.created_at
                ])
            return Response(buf.getvalue(), content_type="text/csv")
        else:
            return Response(SentimentReviewSerializer(SentimentReview.objects.filter(user=request.user), many=True).data)

class SentimentBulkDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request):
        SentimentReview.objects.filter(user=request.user).delete()
        return Response({"deleted": True})