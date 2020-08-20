from rest_framework import generics
from .models import Article
from django.shortcuts import get_object_or_404
from .serializers import ArticleSerializer



class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs.get('article_id'))
