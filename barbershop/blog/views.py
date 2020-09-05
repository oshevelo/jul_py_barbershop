from rest_framework import generics
from django.contrib.auth.models import User
from .models import Article, ArticleTag
from django.shortcuts import get_object_or_404
from .serializers import ArticleSerializer, UserSerializer, ArticleTagSerializer
from rest_framework.pagination import LimitOffsetPagination

# /////////////////////////////////////////////| PAGINATIONS |//////////////////////////////////////////////////////////

class StandartPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 30



# //////////////////////////////////////////////////| VIEWS |///////////////////////////////////////////////////////////

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = StandartPagination

class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs.get('article_id'))



class TaggedArticleList(generics.ListCreateAPIView):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer
    pagination_class = StandartPagination

class TaggedArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer
    def get_object(self):
        return get_object_or_404(ArticleTag, pk=self.kwargs.get('tag_id'))
