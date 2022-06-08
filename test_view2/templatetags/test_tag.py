# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 00:00
# @Author  : Walter
# @File    : test_tag.py
# @License : (C)Copyright Walter
# @Desc    :
# 导入template模块
from django import template

# 定义register变量，固定写法
register = template.Library()


# 函数注册为simple_tag模板标签，并命名
# 函数要注册为simple_tag才能在HTML文件中调用
@register.simple_tag(name="test_simpletag")
def test_simpletag(arg1, arg2, arg3):
    return "这是一个simpletag示例，它接收的参数分别是:{}、{}、{}".format(arg1, arg2, arg3)


# 函数注册为inclusion_tag模板标签，并指明HTML代码片段所在文件的名称
# 函数将会把生成的变量传递给这个HTML文件
@register.inclusion_tag('test_view2/inclusion_tag_html.html')
def test_inclusiontag(name):
    # 定义变量
    name1 = "{}的经历如下：".format(name)
    # 定义变量
    data = ["初级程序员，技术入门", "中级程序员，技术熟练", "高级程序员，技术精湛"]
    # 这些变量会传递给inclusion_tag_html.html文件
    return {"name": name1, "data": data}
