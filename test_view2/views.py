from django import template
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


def del_person(request, personid):
    person_obj = person.objects.get(id=personid)
    # 删除记录对象
    person_obj.delete()
    return redirect('/test_view2/index/')


# 在视图函数中列举各种类型的变量，主要演示它们作为模板变量时在模板文件中显示的形式
def template_test(request):
    # 列表变量
    v_list = ['程序员', '产品经理', '产品销售', '架构师']
    # 字典变量，注意：key名字一定包含在引号中
    v_dic = {"name": "张三", "age": 16, "love": "编程"}

    # 定义一个类，这个类有属性name、language和hair
    # 这个类还有一个方法hope()
    class coder(object):
        # 类的初始化方法，为3个属性赋值
        def __init__(self, name, language, hair):
            self.name = name
            self.language = language
            self.hair = hair

        # 类的方法，定义函数hope()
        def hope(self):
            return '{}的希望是程序少出bug，工作少加班！'.format(self.name)

    # 实例化类，生成类对象
    zhang = coder('张三', 'python', '多')
    # 实例化类，生成类对象
    li = coder('李四', 'php', '不多不少')
    # 实例化类，生成类对象
    wang = coder('王五', 'c#', '少')
    # 建立列表变量coders，把类对象作为列表中的元素
    coders = [zhang, li, wang]
    # 向HTML文件传参数，传递不同类型的变量
    return render(request, 'test_view2/test_template.html', {'v_list': v_list, 'v_dic':
        v_dic, 'coders': coders})


# 自定义模版
def test_filter(request):
    vhair = "fewhair"
    vhair2 = "middlehair"
    num = 4
    age = 80
    user_list = [{"name": "lingming", "age": 18}, {"name": "Tom", "age": 15}, {"name": "John", "age": 17},
                 {"name": "wangwu", "age": 19}]
    return render(request, 'test_view2/test_filter.html',
                  {"hair": vhair, "num": num, "age": age, "user_list": user_list, "hair2": vhair2})


def test_for(request):
    # 定义列表变量
    v_list = ['程序员', '产品经理', '产品销售', '架构师', '老板', '员工']
    return render(request, 'test_view2/test_for.html', {'vlist': v_list})


def test_tag(request):
    return render(request, 'test_view2/test_tag.html')


def test_inclusion_tag(request):
    return render(request, 'test_view2/test_inclusion_tag.html')


def test_mom(request):
    return render(request, 'test_view2/inhert_base.html')

def test_module(request):
    return render(request, 'test_view2/module.html')


def test_fontAwesome(request):
    return render(request, 'test_view2/bootstrapDemo/fontAwesome.html')

def test_base(request):
    return render(request, 'test_view2/bootstrapDemo/base.html')

def test_index(request):
    return render(request, 'test_view2/bootstrapDemo/index.html')


# 从当前目录导入forms文件
from . import forms


def testform(request):
    if request.method == "POST":
        # 通过request.POST为test_form对象赋值
        test_form = forms.test_form(request.POST)
        # 表单校验功能
        if test_form.is_valid():
            # 校验通过的数据存放在cleaned_data中，cleaned_data是字典类型的
            # 因此要用get()函数取值
            account = test_form.cleaned_data.get("account")
            pw = test_form.cleaned_data.get("password")
            if (account == 'test' and pw == '123'):
                return HttpResponse("登录成功")
            else:
                return HttpResponse("用户名或密码错误")
        else:
            return HttpResponse("数据输入不合法")
    # 初始化生成一个test_form对象
    test_form = forms.test_form()
    # 通过render()把testform表单对象传递给test_form
    return render(request, 'test_view2/test_form.html', {'testform': test_form})
