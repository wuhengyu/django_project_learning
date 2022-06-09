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
    path('test_filter/', test_filter),
    path('test_tag/', test_tag),
    path('test_inclusion_tag/', test_inclusion_tag),
    path('test_mom/', test_mom),
    path('test_module/', test_module),
    path('test_fontAwesome/', test_fontAwesome),
    path('test_base/', test_base),
    path('test_index/', test_index),


    path('test_form/', testform),



]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)