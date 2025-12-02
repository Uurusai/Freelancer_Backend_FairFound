from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/auth/', include('account.urls')),
    path('api/v1/users/', include('account.urls')),
    #path('api/v1/freelancers/', include('freelancer_api.urls')),
    path('api/v1/comparisons/', include('comparisons.urls')),
    path('api/v1/sentiment/', include('sentiments.urls')),
    path('api/v1/mentorship/', include('mentorship.urls')),
    path('api/v1/industries/', include('industries.urls')),
    path('api/v1/core/', include('core.urls')),
    path('api/v1/health/', include('core.health_urls')),
]