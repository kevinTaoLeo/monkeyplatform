# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proper(models.Model):
    variable_name=models.CharField(max_length=50,null=True)
    variable_word=models.CharField(max_length=50,null=True)
    variable_date = models.DateTimeField(u'时间', auto_now_add=True, editable=True)
    status=models.IntegerField(default='1')
    def __unicode__(self):
        return self.variable_name
    def __unicode__(self):
        return self.variable_word

