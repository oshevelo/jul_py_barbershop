from rest_framework import serializers
from blog.models import Article, ArticleTag
from django.contrib.auth.models import User
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField


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
    tags = TagListSerializerField(required=False, allow_null=True) 
    class Meta:
        model = Article
        fields = [
            'id',
            'header',
            'body',
            'tags',
            'created_by',
            'created_on',
            'updated_by',
            'updated_on',
        ]


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = [
            'name',
            'articles'
        ]
