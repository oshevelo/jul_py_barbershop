from django.contrib import admin
from .models import Comment, CommentItem

class CommentItemInline(admin.StackedInline):
    model = CommentItem
    extra = 1

class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentItemInline]
    list_display = ["text"]
    ordering = ["text"]
    search_fields = ["text"]


admin.site.register(Comment, CommentAdmin)
