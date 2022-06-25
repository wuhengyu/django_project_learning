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
        # label内容后缀
        label_suffix="：",
        # 指定帮助信息或者字段的描述信息
        # help_text="请输入账号",
        # 设置最小长度为10
        min_length=10,
        # 字段名称
        label="账号",
        # 设置初始值
        initial="admin初始值",
        # 是否可以为空
        required=True,
        # 设置错误信息
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "编码最少10位"
})
    password = forms.CharField(
        label='密码',
        required=True,
        label_suffix="：",
        min_length=10,
        initial="password初始值",
        # widget=forms.widgets.PasswordInput(attrs={'class': 'password'}, render_value=True),
        widget=forms.PasswordInput(attrs={'class': 'password'}, render_value=True),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "密码最少10位"
})


class userinfo(forms.Form):
    name = forms.CharField(label='名字', required=True)
    url = forms.URLField(label='链接', required=True)
    comment = forms.CharField()
    pwd = forms.CharField(
        min_length=8,
        label="密码",
        # widget=forms.widgets.PasswordInput(attrs={'class': 'password'}, render_value=True)
        widget=forms.PasswordInput(attrs={'class': 'password'}, render_value=True)
)
    studentinfo = forms.CharField(
        min_length=10,
        label="学生编码",
        initial="1230000001",
        error_messages={
        "required": "不能为空",
        "invalid": "格式错误",
        "min_length": "编码最少10位"
        }
    )
    # 数值类型字段
    integ = forms.IntegerField(max_value=100, min_value=10)
    fl = forms.FloatField(max_value=199.88, min_value=10.66)
    de = forms.DecimalField(max_value=2199.88, min_value=210.37, max_digits=7, decimal_places=2)

    # 日期时间字段
    # “yyyy-mm-dd”形式，如“2019-08-08”
    date = forms.DateField()
    # “hh:mm”形式，如“12:30”
    time = forms.TimeField()
    # “yyyy-mm-dd hh:mm”形式，如“2019-08-08 12:16”
    dt = forms.DateTimeField()

    # 生成 < select > 标签
    sex = forms.ChoiceField(
        choices=((1, '男'), (2, '女'),),
        initial=1
    )

    Email = forms.EmailField(label='邮箱', required=False)