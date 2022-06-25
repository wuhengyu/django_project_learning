from django.db import models

from django.db import models
# 导入自定义的模块，这个模块将上传文件按一定格式命名并存储
from test_form.utils.rename_upload import RenameUpload


class loguser(models.Model):
    account = models.CharField(max_length=32, verbose_name="账号")
    password = models.CharField(max_length=20, verbose_name="密码")
    email = models.EmailField(verbose_name="邮箱")
    gender = models.CharField(max_length=1)
    hobby = models.CharField(max_length=20)
    hair = models.CharField(max_length=1)
    img = models.ImageField(upload_to='loguser_image', storage=RenameUpload(), blank=True, null=True)
