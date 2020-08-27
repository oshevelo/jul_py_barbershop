from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')
router.register('tag', views.TaggedArticleViewSet, basename='tag')
router.register('user', views.UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls))
]
