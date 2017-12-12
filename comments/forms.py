#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File Name: comments/forms.py
# Author: wangqi
# mail: qi77wang@163.com
# Created Time: 2017年12月07日 星期四 14时49分38秒

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
