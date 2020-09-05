from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from comments.models import CommentItem
from .models import Article, ArticleTag, TaggedArticle


class GenericCommentInline(GenericStackedInline):
    model = CommentItem
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['header', 'body']}),
        ('Tags', {'fields': ['tags']})
    ]
    inlines = [GenericCommentInline]
    list_display = ('header', 'created_on', 'tag_list')
    list_filter = ['created_on', 'tags']
    search_fields = ['header', 'body']
    date_hierarchy = 'created_on'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())



class TaggedArticleInline(admin.StackedInline):
    model = TaggedArticle

class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedArticleInline]
    list_display = ["name", "slug"]
    ordering = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleTag, TagAdmin)
