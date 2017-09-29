# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from forms import  ProerForm
from base import  models
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.core.exceptions import ValidationError
# Create your views here.

each_page=10

@login_required
def proper_save(request):
    if request.method == 'POST':
        ps = ProerForm(request.POST)
        if ps.is_valid():
        # 获取表单信息
            variable_name = ps.cleaned_data['variable_name']
            variable_word = ps.cleaned_data['variable_word']
#        pro_ok = Proper.objects.filter(variable_name__exact == variable_name, variable_name__exact == variable_word)
#        if pro_ok:
        # 将表单写入数据库
            proper = models.Proper()
            is_exist = models.Proper.objects.filter(Q(variable_name=variable_name) | Q(variable_word=variable_word))
            if is_exist:
                return render(request,'base/property_manager.html',{'ps': ps, 'error': ps.errors})
#                   return HttpResponseRedirect('proper_view')
            else:
                proper.variable_name = variable_name
                proper.variable_word = variable_word
                proper.save()
                return HttpResponseRedirect('proper_view')
        else:
            ps = ProerForm()
    return render(request,'base/property_manager.html',{'ps': ps})

@login_required
def proper_view(request):
    if request.method == 'GET':
        pv = models.Proper.objects.all()
        paginator = Paginator(pv,each_page)
        page = request.GET.get('page', 1)

        try:
            show_list = paginator.page(page)
        except PageNotAnInteger:
            show_list = paginator.page(1)
        except (EmptyPage,InvalidPage):
            show_list = paginator.page(paginator.num_pages)
        pv = models.Proper.objects.all()
        return render_to_response('base/property_manager.html',{'show_list': show_list , 'paginator':paginator })