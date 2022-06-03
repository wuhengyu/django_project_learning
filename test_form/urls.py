# -*- coding: utf-8 -*-
# @Time    : 2022/6/3 15:14
# @Author  : Walter
# @File    : urls.py
# @License : (C)Copyright Walter
# @Desc    :

# 导入静态服务函数
from django.conf.urls.static import static
# 导入settings.py文件
from django_project_learning import settings
from . import admin
from django.urls import path
from test_form.views import *

urlpatterns = [

    path('login/', login),

# 用静态服务函数static()指定上传文件URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
