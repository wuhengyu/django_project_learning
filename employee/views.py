from django.shortcuts import render, redirect, HttpResponse
from .models import employee, department, group, employeeinfo


# Create your views here.
# 部门数据表的增、删、改、查
def list_dep_old(request):
    # 取得数据库表全部记录
    dep_list = department.objects.all()
    return render(request, 'test_orm_old/list_dep_old.html', {'dep_list': dep_list})


# views.py第二段代码
def add_dep_old(request):
    # 判断请求方式，如果是POST，说明前端页面要提交数据
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        if dep_name.strip() == '':
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info': '部门名称不能为空！'})
        try:
            # 用create()函数新建一条记录，这条记录会自动保存，不用调用save()函数
            department.objects.create(dep_name=dep_name, dep_script=dep_script)

            # 或者
            # dic = {"dep_name": dep_name, "dep_script": dep_script}
            # department.create(**dic)

            # 或者
            # obj = department(dep_name=dep_name, dep_script=dep_script)
            # obj.save()
            return redirect('/test_orm_old/list_dep_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info': '输入部门名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_dep_old.html')


# views.py第三段代码
def del_dep_old(request, dep_id):
    # 判断请求方式
    if request.method == 'POST':
        # 通过get()函数取得一条记录
        dep_object = department.objects.get(id=dep_id)
        # 删除部门记录
        dep_object.delete()
        return redirect('/test_orm_old/list_dep_old/')
    return render(request, 'test_orm_old/delete_dep_old.html')


# views.py第四段代码
def edit_dep_old(request, dep_id):
    # 判断请求方式
    if request.method == 'POST':
        id = request.POST.get('id')
        # 获取前端页面提交的数据
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        dep_object = department.objects.get(id=id)
        # 给字段赋值
        dep_object.dep_name = dep_name
        dep_object.dep_script = dep_script
        # 保存数据到数据库表
        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object = department.objects.get(id=dep_id)
    return render(request, 'test_orm_old/edit_dep_old.html', {'department': dep_object})


# views.py第五段代码
# 团体数据表的增、删、改、查
def list_group_old(request):
    group_list = group.objects.all()
    return render(request, 'test_orm_old/list_group_old.html', {'group_list': group_list})


def add_group_old(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        # 团体名称group_name为空时，向网页传递错误信息
        if group_name.strip() == '':
            return render(request, 'test_orm_old/add_group.html', {'error_info': '团体名称不能为空！'})
        try:
            group.objects.create(group_name=group_name, group_script=group_script)
            return redirect('/test_orm_old/list_group_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_group_old.html', {'error_info': '输入团体名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_group_old.html')

def del_group_old(request,group_id):
  group_object=group.objects.get(id=group_id)
  group_object.delete()
  return redirect('/test_orm_old/list_group_old/')

def edit_group_old(request,group_id):
  if request.method=='POST':
      id=request.POST.get('id')
      group_name=request.POST.get('group_name')
      group_script=request.POST.get('group_script')
      group_object=group.objects.get(id=id)
      group_object.group_name=group_name
      group_object.group_script=group_script
      group_object.save()
      return redirect('/test_orm_old/list_group_old/')
  else:
      group_object=group.objects.get(id=group_id)
  return render(request,'test_orm_old/edit_group_old.html',{'group':group_object})
