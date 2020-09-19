from rest_framework import serializers
from .models import Article, TaggedArticle, ArticleTag
from django.contrib.auth.models import User
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField
from comments.fields import CommentArticleRelatedField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]



class ArticleSerializer(serializers.ModelSerializer, TaggitSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    comment = CommentArticleRelatedField(required=False, allow_null=True)
    tags = TagListSerializerField(required=False, allow_null=True) 
    class Meta:
        model = Article
        fields = [
            'header',
            'body',
            'tags',
            'created_by',
            'created_on',
            'updated_by',
            'updated_on',
            'comment'
        ]



class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = [
            'name',
            'articles'
        ]
