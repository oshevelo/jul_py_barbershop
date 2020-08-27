from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Article, TaggedArticle, ArticleTag
from taggit.models import Tag
from django.contrib.auth.models import User
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]



class ArticleSerializer(serializers.ModelSerializer, TaggitSerializer):
    tags = TagListSerializerField() 
    created_by = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )
    updated_by = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )
    class Meta:
        model = Article
        fields = [
            'header',
            'body',
            'tags',
            'created_by',
            'created_on',
            'updated_by',
            'updated_on'
        ]



class ArticleTagSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        view_name='article-detail',
        read_only=True,
        many=True
    )
    class Meta:
        model = ArticleTag
        fields = [
            'name',
            'articles'
        ]
