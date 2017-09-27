# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from forms import UserForm
from  models import  User
from django.contrib.auth import get_user_model

from django.template import RequestContext
# Create your views here.

#登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                return render_to_response('base/base.html',{'username':username})
            else:
                return HttpResponseRedirect('/accounts/')
    else:
        uf = UserForm()
    return render_to_response('accounts/index.html',{'uf':uf})









