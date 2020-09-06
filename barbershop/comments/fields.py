from rest_framework import serializers
from .models import Comment, CommentItem
from collections import OrderedDict
from blog.models import Article
import re
import ast
import datetime
from django.contrib.auth.models import User

from .serializers import CommentItemSerializer, CommentSerializer


class CommentArticleRelatedField(serializers.RelatedField):
    queryset = Comment.objects.all()
    
    def to_representation(self, value):
        if isinstance(value, Comment):
            ret = []          
            dct = CommentSerializer(value).data
            for i in dct.keys():
                ret.append((i, str(dct[i])))
            return tuple(ret)
        else:
            data_list = []
            for i in value.all():
                data_list.append(CommentItemSerializer(i).data)
            return data_list
        # raise Exception('Unexpected type')

    def to_internal_value(self, data):
        
        print(data)
        ret = {
            'text': 'gav gav',
            'created_by': OrderedDict([('username', 'Ivan'), ('email', '')]),
            'created_on': datetime.datetime.strptime('2020-09-02T22:57:23.433397+0300', '%Y-%m-%dT%H:%M:%S.%f%z'), 
            'updated_by': OrderedDict([('username', 'Ivan'), ('email', '')]), 
            'updated_on': datetime.datetime.strptime('2020-09-02T22:57:23.433557+0300', '%Y-%m-%dT%H:%M:%S.%f%z')
        }

        return OrderedDict(ret)
            
