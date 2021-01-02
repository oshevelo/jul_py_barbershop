from rest_framework import generics
from blog.models import Article, ArticleTag
from comments.models import CommentItem
from django.shortcuts import get_object_or_404, get_list_or_404
from blog.serializers import ArticleSerializer, ArticleTagSerializer
from comments.serializers import CommentItemSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# /////////////////////////////////////////////| PAGINATIONS |//////////////////////////////////////////////////////////

class StandartPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 30


# //////////////////////////////////////////////////| VIEWS |///////////////////////////////////////////////////////////

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = StandartPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

class ArticleCommentList(generics.ListCreateAPIView):
    serializer_class = CommentItemSerializer
    pagination_class = StandartPagination

    def get_queryset(self):
        return get_list_or_404(CommentItem, object_id=self.kwargs.get('article_id'))

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
