from rest_framework import serializers
from .models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'header',
            'body',
            'pub_date',
            'time_delta'
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'tag_name',
            'articles'
        ]
