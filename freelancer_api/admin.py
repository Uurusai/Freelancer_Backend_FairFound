from django.contrib import admin
from .models import FreelancerProfile, RoadmapMilestone, RankingSnapshot

admin.site.register(FreelancerProfile)
admin.site.register(RoadmapMilestone)
admin.site.register(RankingSnapshot)
# 	search_fields = ("user_profile__user__username", "compare_with__user__username")
# 	list_filter = ("created_at",)

# @admin.register(SWOTAnalysis)
# class SWOTAnalysisAdmin(admin.ModelAdmin):
# 	list_display = ("id", "user_profile", "created_at", "updated_at")
# 	search_fields = ("user_profile__user__username",)
# 	list_filter = ("created_at", "updated_at")

# @admin.register(CareerRoadmap)
# class CareerRoadmapAdmin(admin.ModelAdmin):
# 	list_display = ("id", "user_profile", "visibility_boost", "created_at", "updated_at")
# 	search_fields = ("user_profile__user__username",)
# 	list_filter = ("visibility_boost", "created_at")
