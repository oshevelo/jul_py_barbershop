from django.urls import path
from . import views
from comments import views as comment_views


urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='list'),
    path('articles/<int:article_id>/', views.ArticleDetails.as_view(), name='details'),
    path('articles/<int:article_id>/comments/', views.ArticleCommentList.as_view(), name='list'),
    path('tags/', views.TaggedArticleList.as_view(), name='list'),
    path('tags/<int:tag_id>/', views.TaggedArticleDetails.as_view(), name='details'),
    path('comments/', comment_views.CommentList.as_view(), name='list'),
    path('comment/<int:comment_id>/', comment_views.CommentDetails.as_view(), name='details')
]
