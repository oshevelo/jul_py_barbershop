from django.db import models
from apps_generic.whodidit.models import WhoDidIt, set_who_did_it
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Comment(WhoDidIt):
    text = models.TextField()

    def __str__(self):
        return self.text
    

class CommentItem(models.Model):
    comment_ptr = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        related_name='comment_item',
        blank=True,
        null=True
    )

    content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE,
        related_name='comment',
        blank=True,
        null=True
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field='content_type',
        fk_field='object_id'
    )

    def __str__(self):
        return 'CommentItem {}'.format(self.object_id)

