# -*- coding: utf-8 -*-
# @Time    : 2022/6/2 00:16
# @Author  : Walter
# @File    : test_filter.py
# @License : (C)Copyright Walter
# @Desc    :


# 自定义过滤器
# 取出注册库，固定写法
from django import template

register = template.Library()


# 注册过滤器的名字为coderstatus
# 必须使用这个名字coderstatus
@register.filter(name='coderstatus')
def coder_status(value, arg):
    if value == 'morehair':
        # return "{}是菜鸟程序员".format(arg)
        return "%s是菜鸟程序员" % arg
    if value == "middlehair":
        return "{}是工程师级程序员".format(arg)
    if value == 'fewhair':
        return "{}是资深程序员".format(arg)

