from django.contrib import admin
from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['header', 'body']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('header', 'pub_date', 'body', 'time_delta')
    list_filter = ['pub_date']
    search_fields = ['header', 'body']
    date_hierarchy = 'pub_date'


# class TagAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('General', {'fields': ['tag_name']}),
#         ('Articles', {'fields': ['articles']})
#     ]


admin.site.register(Article, ArticleAdmin)
# admin.site.register(Tag, TagAdmin)