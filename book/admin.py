from django.contrib import admin

# Register your models here.
from . import models


class bookadmin(admin.ModelAdmin):
    # 用出版日期作为导航查询字段
    date_hierarchy = 'publishdate'
    # 设置字段无值时显示的内容
    empty_value_display = '-无值-'
    # 设置author字段的选择方式为水平扩展选择
    filter_horizontal = ('author',)
    # 以下代码在页面上对字段进行分组显示或布局
    fieldsets = (
        (
            '图书信息',
            {'fields': (('title', 'publishdate'), 'publishing', 'author')}),
        (
            '图书简介',
            {'classes': ('collapse',), 'fields': ('descript',)}),)

    # 自定义一个字段
    def descript_str(self, obj):
        # 对字段进行切片，取前20个字符
        return obj.descript[:20]

    # 设置自定义字段名字
    descript_str.short_description = '简介'
    # 设置过滤导航字段
    list_filter = ('title', 'publishing', 'author')
    # 设置查询的字段
    search_fields = ('title', 'publishing__name', 'author__name')
    # 列表显示字段
    list_display = ('title', 'descript_str', 'publishdate', 'publishing',)
    # 显示查询到的记录数
    show_full_result_count = True
    # 设定每页显示6条记录
    list_per_page = 6


admin.site.register(models.book, bookadmin)


# admin.py第二段代码
class publishingadmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_editable = ('address',)
    list_per_page = 10


admin.site.register(models.publishing, publishingadmin)

# admin.py第三段代码
from django.utils.safestring import mark_safe


class authoradmin(admin.ModelAdmin):
    # 自定义字段，使图片带有HTML格式并显示
    def header_data(self, obj):
        # mark_safe()函数避免格式字符被转义，防止HTML代码被转义
        return mark_safe(u'<img src="/media/%s" width="50px" height="30px"/>' % obj.header)

    # 定义字段名字
    header_data.short_description = '简介'
    list_display = ('name', 'email', 'birthday', 'header_data')
    list_per_page = 10


admin.site.register(models.author, authoradmin)
