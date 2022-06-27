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


class loguser_form(forms.Form):
    # 定义id字段，用来保存数据库表的主键值，为了在修改时定位到某条记录
    id = forms.IntegerField(label='', widget=forms.widgets.NumberInput(attrs={'hidden': 'true'}), required=False)
    account = forms.CharField(
        label='账号',
        # 设置标签的属性class、placeholder、autofocus，使界面友好
        widget=forms.widgets.TextInput(attrs={'class': 'form-control', "placeholder": "请输入账号", "autofocus": True}))
    password = forms.CharField(
        label='密码',
        # password字段未设置成Password Input，因为这里是信息输入页面
        # 用户需要看到输入的内容
        widget=forms.widgets.TextInput(attrs={'class': 'form-control', "placeholder": "请输入密码"}))
    email = forms.EmailField(
        label='邮箱',
        widget=forms.widgets.EmailInput(attrs={'class': 'form-control', "placeholder": "请输入邮箱"}))
    gender = forms.ChoiceField(
        # 设置字段选项
        choices=((1, "男"), (2, "女"),),
        label='性别',
        initial='1',
        widget=forms.widgets.RadioSelect())
    hobby = forms.ChoiceField(
        choices=((1, "游泳"), (2, "自行车"), (3, "跑酷"),),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
    hair = forms.ChoiceField(
        label='发量',
        choices=((1, '很多'), (2, '一般'), (3, '很少'),),
        widget=forms.widgets.RadioSelect())
    # 这是一个图片字段，涉及图片上传
    img = forms.ImageField(label='头像', required=False)


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
