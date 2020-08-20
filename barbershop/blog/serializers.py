from rest_framework import serializers
from .models import Article
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
    tags = TagListSerializerField()
    created_by = UserSerializer()
    updated_by = UserSerializer()
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
