#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'taojh'
__mtime__ = '2017/9/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from django.conf.urls import url, include
from base import views


urlpatterns = [
    # url(r'^$', user.user_list, name='accounts'),
    url(r'^proper_manage/proper_save', views.proper_save, name='proper_save'),
    url(r'^proper_manage/proper_view', views.proper_view, name='proper_view'),
]