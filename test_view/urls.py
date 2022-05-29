# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 00:45
# @Author  : Walter
# @File    : urls.py
# @License : (C)Copyright Walter
# @Desc    :
from django.urls import path
from test_view.views import *

urlpatterns = [

    # 响应三剑客
    path('test_views/', hello_view),
    path('Http_Response/', Http_Response),
    path('Http_Response_flush/', Http_Response_flush),
    path('dep/<int:dep_id>/', depdetail, name='depdetail'),
    path('test_redirect1/', test_redirect1),
    path('test_redirect2/', test_redirect2),
    path('test_redirect3/', test_redirect3),
    path('test_redirect4/', test_redirect4),

    # 通用视图
    path('test_templateview/', test_templateview.as_view()),
    path('listviewdemo/',listviewdemo.as_view()),

]