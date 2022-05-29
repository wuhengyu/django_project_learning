# 导入数据模块
from django.db import models
# 导入反向解析函数
from django.urls import reverse


# 在此处编写数据模型代码
# 部门数据模型（部门数据表）
class department(models.Model):
    # 部门名称，为字符类型
    dep_name = models.CharField(max_length=32, verbose_name='部门名称', unique=True, blank=False)
    # 部门备注说明
    dep_script = models.CharField(max_length=60, verbose_name='备注', null=True)

    # 数据模型的get_absolute_url()方法
    # 该函数返回一个URL, 这个URL形如“/dep/1/”
    # 把URL配置项名字和obj的id当作参数反向解析出一个URL并返回给redirect()函数
    def get_absolute_url(self):
        # 反向解析URL，解析成/dep/self.pk/
        # reverse()函数得到URL后去urls.py文件中找匹配关系,找到对应视图函数为depdetail()并执行
        return reverse('depdetail', kwargs={'dep_id': self.pk})


class person(models.Model):
    # 部门名称，为字符类型
    name = models.CharField(max_length=32, verbose_name='部门名称', blank=False)
    # 部门备注说明
    email = models.EmailField(verbose_name='邮箱')
    gender = models.IntegerField(verbose_name='性别')
    head_img = models.ImageField(upload_to='test_view_pic')


class loguser(models.Model):
    # 部门名称，为字符类型
    account = models.CharField(max_length=32, verbose_name='用户名', blank=False)
    # 部门备注说明
    password = models.CharField(max_length=32, verbose_name='密码')
