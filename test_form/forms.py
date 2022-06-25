# -*- coding: utf-8 -*-
# @Time    : 2022/6/3 15:52
# @Author  : Walter
# @File    : forms.py
# @License : (C)Copyright Walter
# @Desc    :
from django import forms

# class login_form(forms.Form):
#     account = forms.CharField(
#         min_length=2,
#         label="账号",
#     )
#     # 要求密码长度最少为6位
#     pwd = forms.CharField(
#         min_length=6,
#         label="密　码",
#         # 设置标签为密码输入形式
#         widget=forms.widgets.PasswordInput(attrs={'class': 'password'}, render_value=True)
#     )
from . import models


class login_form(forms.Form):
    account = forms.CharField(
        min_length=2,
        label="账号",
        # 设置的class样式为form-control，这个是Bootstrap样式
        widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "请输入账号", "autofocus": True})
    )
    pwd = forms.CharField(
        min_length=6,
        label="密码",
        # render_value=True这个设置表示如果输入错误，也要保持输入框的内容不被清除
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码"}, render_value=True)
    )


class loguser_modelform(forms.ModelForm):
    class Meta:
        # 指定数据模型loguser，以loguser类的定义为基础建立表单
        model = models.loguser
        # _all__表示列出所有的字段
        fields = "__all__"
        # 排除hair，email两个字段
        exclude = ['hair', 'email']
        label = {
            'account': '账号',
            'gender': '性别',
            'hobby': '爱好',
            'img': '头像'
        }
