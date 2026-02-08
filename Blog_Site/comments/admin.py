from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at")
    search_fields = ("content",)
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)


