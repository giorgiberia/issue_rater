from django.contrib import admin
from .models import Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'rating', 'created_at')
    search_fields = ('title', 'description')
