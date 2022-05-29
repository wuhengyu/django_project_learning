from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from django.views.generic import ListView, DetailView
from test_view.models import department, person, loguser


def hello_view(request):
    # 取出当前日期
    vnow = datetime.datetime.now().date()
    # 组合一个HTML格式的文本
    rep = "<div align='center'>" \
          "<h1>你好，欢迎你浏览本页面</h1>" \
          "<hr>当前日期是%s</div>" % vnow
    # 通过Http Response()函数返回一个Http Response对象
    # 　Http Response()函数把传给它的文本解析成HTML格式发送给网页
    return HttpResponse(rep)


def Http_Response(request):
    # HttpResponse()
    response = HttpResponse("hello,world", content_type="text/plain", charset='gb2312')

    # write()
    response.write("这是一行")
    response.write("这是另一行")

    # writelines()
    lines = ["这是一行2", "这是第二行2"]
    response.writelines(lines)

    # 清空HttpResponse实例的内容
    response.flush()
    return response


# 清空Http Response实例的内容
def Http_Response_flush(request):
    response = HttpResponse()
    response.write("<p>这是一行</p>")
    response.flush()
    return response


def depdetail(request, dep_id):
    # 根据传入的参数值取出一条记录
    obj = department.objects.get(id=dep_id)
    # 返回Http Response对象
    return HttpResponse('部门：' + obj.dep_name + '，备注：' + obj.dep_script)


# 重定向redirect第一种参数
def test_redirect1(request):
    dep_obj = department.objects.get(id=1)
    # 用redirect()重定向，参数是数据模型对象，所以重定向到数据模型get_absolute_url生成的URL
    # 这个URL对应视图函数depdetail(),实际上调用这个函数
    return redirect(dep_obj)


# 重定向redirect第二种参数
def test_redirect2(request):
    # 视图函数depdetail()有参数dep_id
    return redirect('depdetail', dep_id=1)


# 重定向redirect第三种参数
def test_redirect3(request):
    return redirect('http://127.0.0.1:8000/test_view/dep/1/')


# 重定向redirect第四种参数
def test_redirect4(request):
    return redirect('/test_view/dep/1/')


from django.views.generic import TemplateView


# 视图继承于TemplateView
class test_templateview(TemplateView):
    # 设置模板文件
    template_name = 'test_view/test_tmp.html'

    # 重写父类get_context_data()方法, 生成的模板变量字典context
    def get_context_data(self, **kwargs):
        context = super(test_templateview, self).get_context_data(**kwargs)
        # 增加一个模板变量test
        context['test'] = '这是一个要传递的变量test'
        return context


# 视图继承于ListView
class test_listview(ListView):
    # 设置数据模型, 相等于dep_list = models.department.objects.all()
    # 需要过滤条件或者对数据进行有条件选取时，需要通过重写ListView中的get_queryset()方法来实现
    model = department
    # 或者
    # model = department.objects.all()
    # 设置模板文件
    template_name = "test_view/test_listview.html"
    # 设置模板变量
    context_object_name = "dep_list"


# 视图继承于ListView
class listviewdemo(ListView):
    # 设置模板文件
    template_name = "test_view/listviewdemo.html"

    # 设置模板变量，由于没有指定 model 属性，模板变量person_list与get_queryset()函数的返回值对应
    # context_object_name = "person_list"

    # person_list变量存储的get_queryset()函数的返回值
    # 重写get_queryset()，取person中性别为女的人员，gender值为'2'
    def get_queryset(self):
        # 按照gender=’2’过滤数据
        personlist = person.objects.filter(gender='2')
        return personlist

    # 重写父类的get_context_data()，增加模板变量loguser
    def get_context_data(self, **kwargs):
        kwargs['loguser'] = loguser.objects.all().first()
        # 继承父类模板变量的属性，返回这一模板变量（字典类型）
        return super(listviewdemo, self).get_context_data(**kwargs)


# 视图继承于DetailView
class test_detailview(DetailView):
    # 设置数据模型
    model = person
    # 设置模板文件
    template_name = 'test_view/testdetail.html'
    # 设置模板变量
    context_object_name = 'person'
    # 在urls.py文件的urlpattern定义的URL正则表达式中的实名参数person_id
    pk_url_kwarg = 'person_id'


# 视图继承于DetailView
class detailviewdemo(DetailView):
    model = person
    template_name = 'test_view/testdetail.html'
    context_object_name = 'person'
    # 指定获取数据模型的单条数据
    # urls.py文件的urlpattern 列表里的URL表达式中的实名参数为person_id
    pk_url_kwarg = 'person_id'

    def get_object(self, queryset=None):
        # 调用父类的get_object()
        # 调用父类的get_object()生成一条数据记录对象
        # 这个方法要返回一个数据记录
        obj = super(detailviewdemo, self).get_object()
        if obj.gender == '1':
            obj.gender = '男'
        else:
            obj.gender = '女'
        return obj

    def get_context_data(self, **kwargs):
        # 增加一个变量test
        kwargs['test'] = '这是一个DetailView类通用视图生成的页面'
        return super(detailviewdemo, self).get_context_data(**kwargs)
