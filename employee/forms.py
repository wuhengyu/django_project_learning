# -*- coding: utf-8 -*-
# @Time    : 2022/6/11 19:17
# @Author  : Walter
# @File    : forms.py
# @License : (C)Copyright Walter
# @Desc    :
# 导入表单相关的模块
from django import forms


# 定义表单要继承Form类
class test_form(forms.Form):
    # lable是字段显示名称
    account = forms.CharField(
        # 设置最小长度为10
        min_length=10,
        # 字段名称
        label="账号",
        # 设置初始值
        initial="admin初始值",
        # 设置错误信息
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "编码最少10位"
})
    password = forms.CharField(label='密码')


class userinfo(forms.Form):
    name = forms.CharField(label='名字')
    url = forms.URLField(label='链接', required=False)
    comment = forms.CharField()
    pwd = forms.CharField(
        min_length=8,
        label="密码",
        # widget=forms.widgets.PasswordInput(attrs={'class': 'password'}, render_value=True)
        widget=forms.PasswordInput(attrs={'class': 'password'}, render_value=True)
    )