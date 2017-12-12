#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File Name: urls.py
# Author: wangqi
# mail: qi77wang@163.com
# Created Time: 2017年12月05日 星期二 16时25分39秒

from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
