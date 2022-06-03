# -*- coding: utf-8 -*-
# @Time    : 2022/6/3 15:05
# @Author  : Walter
# @File    : rename_upload.py
# @License : (C)Copyright Walter
# @Desc    :
# 导入文件存储类
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class RenameUpload(FileSystemStorage):

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # 初始化
        super(RenameUpload, self).__init__(location, base_url)

    # 重写 _save()方法, 参数name为上传文件名称
    def _save(self, name, content):
        # 导入要用到的模块：文件操作模块、时间模块、随机数模块
        import os, time, random
        # 取得文件扩展名
        ext = os.path.splitext(name)[1]
        # 取得文件所在的目录
        d = os.path.dirname(name)
        # 按照一定的格式命名文件，“年月日时分秒-随机数”
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 100)
        # 给文件加上扩展名，形成完整的文件名
        name = os.path.join(d, fn + ext)
        # 调用父类方法
        return super(RenameUpload, self)._save(name, content)
