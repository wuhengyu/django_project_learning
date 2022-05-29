from django.shortcuts import render, redirect
from test_view2.models import loguser


# Create your views here.
def login(request):
    # 判断请求方式，如果是POST表示数据提交到后端
    if request.method == 'POST':
        # 取得表单提交的account值
        account = request.POST.get('account')
        # 取得表单提交的password值
        password = request.POST.get('password')
        # 勾选了checkbox，get()取得的值是字符串on，未勾选则值是None
        remember = request.POST.get('remember')
        # 数据库查询用户
        obj_loguser = loguser.objects.filter(account=account, password=password).first()
        if obj_loguser:
            rep = redirect('/test_view2/index/')
            if remember == 'on':
                rep.set_cookie('account', account, max_age=60 * 60 * 8)
                return rep
            else:
                errmsg = '用户名或密码错误！'
            return render(request, 'test_view2/login.html', {'errmsg': errmsg})
    # 第二个参数是空字符，表示如果取不到值，就返回一个空字符给account
    account = request.COOKIES.get('account', '')
    return render(request, 'test_view2/login.html', {'account_two': account})
