from django.shortcuts import render

from django.shortcuts import render, redirect
from . import forms
from . import models


def login(request):
    if request.method == 'POST':
        # 用POST提交的数值给Form对象赋值
        form_obj = forms.login_form(request.POST)
        # 对提交的数据进行校验
        if form_obj.is_valid():
            account = form_obj.cleaned_data['account']
            pwd = form_obj.cleaned_data['pwd']
            user_obj = models.loguser.objects.filter(account=account, password=pwd).first()
            if user_obj:
                # 登录成功进入账号列表页面（list_loguser）
                return redirect('/list_loguser/')
            else:
                # 用户或密码不对，把错误信息和Form对象传给login.html页面
                error = '用户不存在或密码错误！'
                return render(request, 'test_form/login.html', {'form_obj': form_obj, 'errmsg': error})
        else:
            # 未通过校验，把Form对象传给login.html页面
            return render(request, 'test_form/login.html', {'form_obj': form_obj})
    # 第一次打开网页，先生成一个Form对象
    form_obj = forms.login_form()
    # 把Form对象传到页面文件
    return render(request, 'test_form/login.html', {'form_obj': form_obj})
