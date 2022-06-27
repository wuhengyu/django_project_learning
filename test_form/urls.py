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
from django.urls import path
from test_form.views import *

urlpatterns = [
    path('login/', login),
    path('list_loguser/', list_loguser),
    path('add_loguser/', add_loguser),
    path('edit_loguser/<int:loguser_id>/', edit_loguser),
    path('del_loguser/<int:loguser_id>/', del_loguser),

# 用静态服务函数static()指定上传文件URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
