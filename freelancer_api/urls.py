from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'profile', views.UserProfileViewSet, basename='profile')
router.register(r'compare', views.ProfileComparisonViewSet, basename='compare')
router.register(r'swot', views.SWOTAnalysisViewSet, basename='swot')
router.register(r'roadmap', views.CareerRoadmapViewSet, basename='roadmap')
router.register(r'rank', views.RankingViewSet, basename='rank')
router.register(r'skills', views.SkillViewSet, basename='skills')

urlpatterns = [
    path('api/freelancers/', include(router.urls)),
    path('api/auth/signup/', views.SignUpView.as_view(), name='auth-signup'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='auth-login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='auth-refresh'),
    path('api/auth/logout/', views.LogoutView.as_view(), name='auth-logout'),
]