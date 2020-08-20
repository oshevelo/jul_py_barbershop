from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('<int:article_id>/', views.ArticleDetails.as_view(), name='details'),
    # path('tag/', views.TagList.as_view(), name='list'),
    # path('tag/<int:tag_id>/', views.TagDetails.as_view(), name='details')
]