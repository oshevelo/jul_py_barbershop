from rest_framework.serializers import RelatedField
from blog.models import Article
from blog.serializers import ArticleSerializer


# class CommentListRelatedField(RelatedField):
    
#     def to_representation(self, value):
#         if isinstance(value, Comment):
#             ret = []          
#             dct = CommentSerializer(value).data
#             for i in dct.keys():
#                 ret.append((i, str(dct[i])))
#             return tuple(ret)
#         else:
#             data_list = []
#             for i in value.all():
#                 data_list.append(CommentItemSerializer(i).data)
#             return data_list
#         # raise Exception('Unexpected type')

#     def to_internal_value(self, data):
#         ret = literal_eval(data)
#         return ret[0][1]


class ContentObjectRelatedField(RelatedField):

    def to_representation(self, value):
        if isinstance(value, Article):
            # print('\nREPRESENTATION --> {}\n'.format(ArticleSerializer(value).data))
            return ArticleSerializer(value).data['header']


    def to_internal_value(self, data):
        print('\nINTERNAL VALUE --> {}\n'.format(data))