# -*- coding: utf-8 -*-
# @Time    : 2022/6/3 15:52
# @Author  : Walter
# @File    : forms.py
# @License : (C)Copyright Walter
# @Desc    :
from django import forms


class login_form(forms.Form):
    account = forms.CharField(min_length=2, label="账号", )
    # 要求密码长度最少为6位
    pwd = forms.CharField(min_length=6, label="密　码",
                          # 设置标签为密码输入形式
                          widget=forms.widgets.PasswordInput(attrs={'class': 'password'}, render_value=True)
                          )
