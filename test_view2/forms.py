# -*- coding: utf-8 -*-
# @Time    : 2022/6/3 11:27
# @Author  : Walter
# @File    : forms.py
# @License : (C)Copyright Walter
# @Desc    :
# 导入表单相关的模块
from django import forms


# 定义表单要继承Form类
class test_form(forms.Form):
    # lable是字段显示名称
    account = forms.CharField(label="账号")
    password = forms.CharField(label='密码')
