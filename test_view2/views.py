from django.http import HttpResponse
from django.shortcuts import render, redirect
from test_view2.models import loguser, person


# Create your views here.
# 如果不勾选时，就不设置cookie，取到的cookie用户名就为空，登录界面就不显示取到到用户名
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
            # 与urls.py文件中URL配置项中的URL正则表达式相关联，前面要加上“/”
            rep = redirect('/test_view2/index/')
            if remember == 'on':
                # 生效时间为8小时, 在8小时内登录，这个值会随请求提交到服务端
                rep.set_cookie('account', account, max_age=60 * 60 * 8)
            # 返回的HttpResponse对象
            return rep
        else:
            errmsg = '用户名或密码错误！'
            return render(request, 'test_view2/login.html', {'errmsg': errmsg})
    # 第二个参数是空字符，表示如果取不到值，就返回一个空字符给account
    account = request.COOKIES.get('account', '')
    return render(request, 'test_view2/login.html', {'account_two': account})


def index(request):
    person_list = person.objects.all()
    return render(request, 'test_view2/index.html', {'person_list': person_list})


def add_person(request):
    if request.method == "POST":
        # 取得姓名
        name = request.POST.get("name")
        # 取得邮箱地址
        email = request.POST.get("email")
        # 取得性别值
        gender = request.POST.get("gender")
        # 图片文件从request.FILES中取值
        head_img = request.FILES.get('head_img')
        # 文件类型从request.FILES中取值
        attachment = request.FILES.get('attachment')
        # print(attachment)
        # 生成一条记录
        person.objects.create(name=name, email=email,
                                           gender=gender, head_img=head_img, attachment=attachment)
        # 重定向
        return redirect('/test_view2/index/')
    return render(request, 'test_view2/add_person.html')


def edit_person(request, personid):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get("name")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        head_img = request.FILES.get('head_img')
        attachment = request.FILES.get('attachment')
        person_obj = person.objects.get(id=id)
        person_obj.name = name
        person_obj.email = email
        person_obj.gender = gender
        # 判断前端网页传入值是否为空
        if head_img:
            # 头像文件有值时才修改数据字段的值
            person_obj.head_img = head_img
        # 判断前端网页传入值是否为空
        if attachment:
            # 上传附件有值时才修改数据字段的值
            person_obj.attachment = attachment
            person_obj.save()
        return redirect('/test_view2/index/')
        person_obj = person.objects.get(id=personid)
    return render(request, 'test_view2/edit_person.html', {'person': person_obj})
