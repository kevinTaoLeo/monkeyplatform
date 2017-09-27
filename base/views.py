# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from  base.models import  Proper
from forms import  ProerForm
# Create your views here.

@login_required
def proper_save(request):
    if request.method == 'POST':
        ps = ProerForm(request.POST)
    if ps.is_valid():
        # 获取表单信息
        variable_name = form.cleaned_data['variable_name']
        variable_word = form.cleaned_data['variable_word']
#        pro_ok = Proper.objects.filter(variable_name__exact == variable_name, variable_name__exact == variable_word)
#        if pro_ok:
        # 将表单写入数据库
        proper = Proper()
        proper.variable_name = variable_name
        proper.variable_word = variable_word
        proper.save(commit=False)
        return HttpResponseRedirect('.')
    else:
        ps = ProerForm()
    return render(request,'base/property_manager.html',{'ps': ps})

@login_required
def proper_view(request):
    if request.method == 'GET':
        pv = ProerForm(request.GET)
        return render(request,'base/property_manager.html',{'pv': pv})