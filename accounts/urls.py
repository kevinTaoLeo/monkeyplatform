#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from accounts import views


urlpatterns = [
    # url(r'^$', user.user_list, name='accounts'),
    url(r'^$', views.login, name='login'),
]