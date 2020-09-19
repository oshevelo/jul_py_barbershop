from django.db import models
from django.utils import timezone


from taggit.managers import TaggableManager
from taggit.models import ItemBase, TagBase
from comments.models import CommentItem, Comment
from django.contrib.contenttypes.fields import GenericRelation
from apps_generic.whodidit.models import WhoDidIt, set_who_did_it


class ArticleTag(TagBase):
    articles = models.ManyToManyField(
        to='Article',
        through='TaggedArticle',
        through_fields=('tag', 'content_object')
    )


class TaggedArticle(ItemBase):
    content_object = models.ForeignKey(
        to='Article',
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        to=ArticleTag,
        related_name="%(app_label)s_%(class)s_items", 
        on_delete=models.CASCADE
    )


class Article(WhoDidIt):
    header = models.CharField(max_length=200)
    body = models.TextField()
    tags = TaggableManager(through=TaggedArticle)
    comment = GenericRelation(
        to=CommentItem,
        blank=True,
        null=True
    )


    def __str__(self):
        return self.header 

