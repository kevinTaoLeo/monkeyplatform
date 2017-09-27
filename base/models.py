# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proper(models.Model):
    variable_name=models.IPAddressField(unique=True)
    variable_word=models.CharField(max_length=50,null=True)
    status=models.IntegerField(default='1')
