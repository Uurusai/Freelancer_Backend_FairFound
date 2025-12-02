from django.urls import path
from .views import SuggestionsView

urlpatterns = [
    path("freelancers/suggestions/", SuggestionsView.as_view()),
]