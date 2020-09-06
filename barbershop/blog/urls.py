from django.urls import path, include
from . import views


urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='list'),
    path('articles/<int:article_id>/', views.ArticleDetails.as_view(), name='details'),
    path('tags/', views.TaggedArticleList.as_view(), name='list'),
    path('tags/<int:tag_id>/', views.TaggedArticleDetails.as_view(), name='details'),
]
