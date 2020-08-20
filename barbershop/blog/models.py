from django.db import models
from django.utils import timezone


from taggit.managers import TaggableManager
from apps_generic.whodidit.models import WhoDidIt, set_who_did_it



class Article(WhoDidIt):
    header = models.CharField(max_length=200)
    body = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.header 
