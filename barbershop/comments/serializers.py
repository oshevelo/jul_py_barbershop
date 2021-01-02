from rest_framework import serializers
from comments.models import Comment, CommentItem
from django.contrib.auth.models import User
from comments.fields import ContentObjectRelatedField
from blog.models import Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'created_by',
            'created_on',
            'updated_by',
            'updated_on'   
        ]


class CommentItemSerializer(serializers.ModelSerializer):
    comment_ptr = CommentSerializer()
    content_object = ContentObjectRelatedField(read_only=True)
    class Meta:
        model = CommentItem
        fields = [
            'comment_ptr',
            'content_object'
        ]

    def create(self, data):
        """
            Blog supported only
        """
        comment = Comment.objects.create(
            text=data['comment_ptr']['text']
        )
        article = Article.objects.get(pk=self.context['view'].kwargs.get('article_id'))
        comment_item = CommentItem.objects.create(
            comment_ptr=comment,
            content_object=article
        )
        return comment_item

