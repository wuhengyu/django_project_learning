from django.db import models

# Create your models here.
from django.db import models


class loguser(models.Model):
    account = models.CharField(max_length=32, verbose_name="登录账号")
    password = models.CharField(max_length=20, verbose_name="密码")


class person(models.Model):
    # 姓名
    name = models.CharField(max_length=32, verbose_name='姓名')
    # 邮箱
    email = models.EmailField(verbose_name="邮箱")
    # 性别，通过choices限定字段取值范围
    gender = models.CharField(max_length=1, choices=(("1", "男"), ("2", "女"),), verbose_name='性别')
    # 头像，upload_to指定图片上传的途径，如果不存在则自动创建
    head_img = models.ImageField(upload_to='headimage', blank=True, null=True, verbose_name='头像')
    # 附件，文件类型字段, 存储在static/media/ + filedir/文件夹中
    attachment = models.FileField(upload_to='filedir', blank=True, null=True, verbose_name='附件')
