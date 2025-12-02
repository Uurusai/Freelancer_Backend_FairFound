from django.contrib import admin
from .models import MentorshipRequest, MentorshipMessage

admin.site.register(MentorshipRequest)
admin.site.register(MentorshipMessage)
