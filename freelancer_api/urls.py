from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profile', views.UserProfileViewSet, basename='profile')
router.register(r'compare', views.ProfileComparisonViewSet, basename='compare')
router.register(r'swot', views.SWOTAnalysisViewSet, basename='swot')
router.register(r'roadmap', views.CareerRoadmapViewSet, basename='roadmap')
router.register(r'rank', views.RankingViewSet, basename='rank')

urlpatterns = [
    path('api/freelancers/', include(router.urls)),
]