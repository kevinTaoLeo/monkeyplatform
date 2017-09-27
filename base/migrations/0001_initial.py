# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_name', models.CharField(max_length=50, null=True)),
                ('variable_word', models.CharField(max_length=50, null=True)),
                ('variable_date', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
                ('status', models.IntegerField(default='1')),
            ],
        ),
    ]