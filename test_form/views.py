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
                return redirect('/test_form/list_loguser/')
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


def list_loguser(request):
    users = models.loguser.objects.all()
    return render(request, 'test_form/list_loguser.html', {'usr_list': users})


def add_loguser(request):
    if request.method == 'POST':
        # 由于有上传图片文件，所以参数中增加request.FILES
        form_obj = forms.loguser_form(request.POST or None, request.FILES or None)
        # 表单数据校验
        if form_obj.is_valid():
            # 在数据库表中新增一条记录
            loguser_obj = models.loguser.objects.create(
                account=form_obj.cleaned_data['account'],
                password=form_obj.cleaned_data['password'],
                email=form_obj.cleaned_data['email'],
                gender=form_obj.cleaned_data['gender'],
                hobby=form_obj.cleaned_data['hobby'],
                hair=form_obj.cleaned_data['hair'],
                img=form_obj.cleaned_data['img']
            )
            # 增加记录后，重新定向到列表页面
            return redirect('/test_form/list_loguser/')
        else:
            # 数据未通过校验，把loguser_form对象传给增加页面
            return render(request, 'test_form/add_loguser.html', {'formobj': form_obj})
    # 第一次打开页面，初始化一个空的表单对象
    form_obj = forms.loguser_form()
    # 定向到增加页面，并传递参数
    return render(request, 'test_form/add_loguser.html', {'formobj': form_obj})


def edit_loguser(request, loguser_id):
    if request.method == 'POST':
        # 由于已上传图片文件，所以在参数中增加request.FILES
        form_obj = forms.loguser_form(request.POST or None, request.FILES or None)
        if form_obj.is_valid():
            # 取出id
            id = form_obj.cleaned_data['id']
            # 取出id对应的记录
            loguser_obj = models.loguser.objects.get(id=id)
            loguser_obj.account = form_obj.cleaned_data['account']
            loguser_obj.password = form_obj.cleaned_data['password']
            loguser_obj.email = form_obj.cleaned_data['email']
            loguser_obj.gender = form_obj.cleaned_data['gender']
            loguser_obj.hobby = form_obj.cleaned_data['hobby']
            loguser_obj.hair = form_obj.cleaned_data['hair']
            loguser_obj.img = form_obj.cleaned_data['img']
            # 如果图片文件为空，是因为没有上传新的文件
            # 需要从预先保存了图片地址的字段img1中取值
            if not loguser_obj.img:
                loguser_obj.img = request.POST.get('img1')
                loguser_obj.save()
                imgname = loguser_obj.img
                return render(request, 'test_form/edit_loguser.html', {'formobj': form_obj, 'img': imgname})
        else:
            return render(request, 'test_form/add_loguser.html', {'formobj': form_obj})
    # 请求方式不是POST，执行以下代码
    # 取得的值，以字典集合的形式存在obj_list中
    obj_list = models.loguser.objects.filter(id=loguser_id).values('id', 'account', 'password', 'email',
                                                                   'gender', 'hobby', 'hair', 'img')
    # 取出第一个字典
    dic = obj_list[0]
    # imgname保存img字段的值
    imgname = dic['img']
    # 用字典值给loguser_form对象赋值
    form_obj = forms.loguser_form(initial=dic)
    return render(request, 'test_form/edit_loguser.html', {'formobj': form_obj, 'img': imgname})


def del_loguser(request, loguser_id):
    obj=models.loguser.objects.get(id=loguser_id)
    obj.delete()
    return redirect('/test_form/list_loguser/')
