"""
URL configuration for freelancer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("account.urls")),
    # path("api/users/", include("account.user_urls")),
    path("api/freelancers/", include("freelancer_api.urls")),
    path("api/comparisons/", include("comparisons.urls")),
    path("api/sentiment/", include("sentiments.urls")),
    path("api/mentorship/", include("mentorship.urls")),
    path("api/industries/", include("industries.urls")),
    path("api/core/", include("core.urls")),
    # Health check
    path("api/health/", include("core.health_urls"))
]
