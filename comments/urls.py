#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File Name: comments/urls.py
# Author: wangqi
# mail: qi77wang@163.com
# Created Time: 2017年12月07日 星期四 15时49分46秒

from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
