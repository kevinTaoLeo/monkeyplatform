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

from django import forms


class ProerForm(forms.Form):
    variable_name = forms.CharField(label='配置名：',max_length=100)
    variable_word = forms.CharField(label='配置值：',max_length=100)

#    def clean_variable_name(self):
#        variable_name = self.cleaned_data['variable_name']
#        is_exist = models.Proper.objects.filter(Q(variable_name=variable_name) | Q(variable_word=variable_word))