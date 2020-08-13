from django.db import models
from django.utils import timezone

import datetime


class Article(models.Model):
    header = models.CharField(max_length=200)
    # own_tag = models.ManyToManyField('Tag')
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def time_delta(self):

        def timeStringFormating(string):
            string = string.split(':')
            measures = [' hours, ', ' min, ', ' sec']
            val = list(map((lambda x, y: (x + y) if int(x) != 0 else ''), string, measures))
            if val[1] is not '':
                return val[0] + val[1]
            elif val[0] is not '':
                return val[0]
            else:
                return val[2]

        delta = timezone.now() - self.pub_date
        stringTimeDate = str(delta)[:-7]
        listTimeDate = stringTimeDate.split(', ')
        if len(listTimeDate) == 1:
            return timeStringFormating(listTimeDate[0])
        else:
            return listTimeDate[0] + ', ' + timeStringFormating(listTimeDate[1])

    def __str__(self):
        return self.header 
        
        
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    articles = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name
