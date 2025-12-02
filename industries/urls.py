from django.urls import path
from .views import IndustryListView, IndustryDetailView

urlpatterns = [
    path("", IndustryListView.as_view()),      # GET /industries/
    path("<slug:slug>/", IndustryDetailView.as_view()),  # GET /industries/{slug}/
]