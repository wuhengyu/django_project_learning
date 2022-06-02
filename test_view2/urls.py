# -*- coding: utf-8 -*-
# @Time    : 2022/5/29 23:51
# @Author  : Walter
# @File    : urls.py
# @License : (C)Copyright Walter
# @Desc    :
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from test_view2.views import *
urlpatterns = [
    # # 登录
    path('login/', login),
    # # 主页，人员列表
    path('index/', index),
    # # 增加人员
    path('add_person/', add_person),
    # # 删除人员
    path('del_person/<int:personid>/', del_person),
    # # 修改人员
    path('edit_person/<int:personid>/', edit_person),

    # 模版变量
    path('template_test/', template_test),
    path('test_filter/', test_filter),
    path('test_for/', test_for),



]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)