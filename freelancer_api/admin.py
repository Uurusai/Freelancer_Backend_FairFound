#not needed


# from django.contrib import admin
# from .models import Skill, UserProfile, ProfileComparison, SWOTAnalysis, CareerRoadmap

# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
# 	list_display = ("id", "name")
# 	search_fields = ("name",)

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
# 	list_display = ("id", "user", "pricing", "pseudo_rank", "rating")
# 	search_fields = ("user__username", "user__email")
# 	list_filter = ("rating",)

# @admin.register(ProfileComparison)
# class ProfileComparisonAdmin(admin.ModelAdmin):
# 	list_display = ("id", "user_profile", "compare_with", "comparison_score", "created_at")
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
