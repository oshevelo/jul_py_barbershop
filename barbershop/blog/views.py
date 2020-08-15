from rest_framework import generics
from .models import Article, Tag
from django.shortcuts import get_object_or_404
from .serializers import ArticleSerializer, TagSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs.get('article_id'))


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_object(self):
        return get_object_or_404(Tag, pk=self.kwargs.get('tag_id'))