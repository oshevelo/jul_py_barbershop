from rest_framework import viewsets
from django.contrib.auth.models import User  
from .models import Article, ArticleTag
from django.shortcuts import get_object_or_404
from .serializers import ArticleSerializer, UserSerializer, ArticleTagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TaggedArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


