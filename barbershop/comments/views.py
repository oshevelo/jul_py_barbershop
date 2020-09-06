from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .models import Comment
from django.shortcuts import get_object_or_404
from .serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_object(self):
        return get_object_or_404(Comment, pk=self.kwargs.get('comment_id'))
