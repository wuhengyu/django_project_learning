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
            return render(request, 'test_orm_old/add_group_old.html', {'error_info': '团体名称不能为空！'})
        try:
            group.objects.create(group_name=group_name, group_script=group_script)
            return redirect('/test_orm_old/list_group_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_group_old.html', {'error_info': '输入团体名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_group_old.html')


def del_group_old(request, group_id):
    # 判断请求方式
    if request.method == 'POST':
        # 通过get()函数取得一条记录
        group_object = group.objects.get(id=group_id)
        # 删除部门记录
        group_object.delete()
        return redirect('/test_orm_old/list_group_old/')
    return render(request, 'test_orm_old/delete_group_old.html')


def edit_group_old(request, group_id):
    if request.method == 'POST':
        # get获取的是<input>标签中属性name的值
        id = request.POST.get('id')
        group_name = request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        group_object = group.objects.get(id=id)
        group_object.group_name = group_name
        group_object.group_script = group_script
        group_object.save()
        return redirect('/test_orm_old/list_group_old/')
    else:
        group_object = group.objects.get(id=group_id)
    return render(request, 'test_orm_old/edit_group_old.html', {'group': group_object})


# views.py第六段代码
# employeeinfo增、删、改、查
# 员工补充信息列表
def list_employeeinfo_old(request):
    info_list = employeeinfo.objects.all()
    return render(request, 'test_orm_old/list_employeeinfo_old.html', {'info_list': info_list})


# 增加一条员工补充信息记录
def add_employeeinfo_old(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if phone.strip() == '':
            return render(request, 'test_orm_old/add_employeeinfo_old.html',
                          {'error_info': '电话号码不能为空！'})
        try:
            employeeinfo.objects.create(phone=phone, address=address)
            return redirect('/test_orm_old/list_employeeinfo_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_employeeinfo_old.html', {'error_info': '信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_employeeinfo_old.html')


# 删除一条员工补充信息记录
def del_employeeinfo_old(request, info_id):
    if request.method == 'POST':
        info_object = employeeinfo.objects.get(id=info_id)
        info_object.delete()
        return redirect('/test_orm_old/list_employeeinfo_old/')
    return render(request, 'test_orm_old/delete_employeeinfo_old.html')


# 修改一条员工补充信息记录
def edit_employeeinfo_old(request, info_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        info_object = employeeinfo.objects.get(id=id)
        info_object.phone = phone
        info_object.address = address
        info_object.save()
        return redirect('/test_orm_old/list_employeeinfo_old/')
    else:
        info_object = employeeinfo.objects.get(id=info_id)
    return render(request, 'test_orm_old/edit_employeeinfo_old.html', {'info': info_object})


# views.py第七段代码
def list_employee_old(request):
    # 取出employee数据表中全部记录
    emp = employee.objects.all()
    # 它是一个Django QuerySet对象集
    # 外键dep、多对多键group、一对一键info这些关联关系也包含在emp对象中，因为Django ORM会自动把关联关系也放在Query Set对象中
    return render(request, 'test_orm_old/list_employee_old.html', {'emp_list': emp})


def delete_employee_old(request, emp_id):
    # 取出主键值等于emp_id的记录对象
    emp = employee.objects.get(id=emp_id)
    # 删除记录对象
    emp.delete()
    return redirect('/test_orm_old/list_employee_old')


# views.py第八段代码
def add_employee_old(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        dep = request.POST.get("dep")
        info = request.POST.get("info")
        salary = request.POST.get("salary")
        # 取得多个值
        groups = request.POST.getlist("group")
        new_emp = employee.objects.create(name=name, email=email,
                                          salary=salary, dep_id=dep, info_id=info)
        # 给多对多键字段赋值
        # 多对多键group涉及多个值，因些在生成一条记录new_emp后，需通过new_emp.group.set(groups)进行赋值
        new_emp.group.set(groups)
        return redirect('/test_orm_old/list_employee_old/')
    dep_list = department.objects.all()
    group_list = group.objects.all()
    info_list = employeeinfo.objects.all()
    return render(request, 'test_orm_old/add_employee_old.html',
                  {'dep_list': dep_list, 'group_list': group_list, 'info_list': info_list})


# views.py第九段代码
def edit_employee_old(request, emp_id):
    if request.method == "POST":
        # 取值
        id = request.POST.get('id')
        name = request.POST.get("name")
        email = request.POST.get("email")
        dep = request.POST.get("dep")
        info = request.POST.get("info")
        groups = request.POST.getlist("group")
        # 设值
        emp = employee.objects.get(id=id)
        emp.name = name
        emp.email = email
        emp.dep_id = dep
        emp.info_id = info
        emp.group.set(groups)
        # 执行
        emp.save()
        return redirect('/test_orm_old/list_employee_old/')
    emp = employee.objects.get(id=emp_id)
    dep_list = department.objects.all()
    group_list = group.objects.all()
    info_list = employeeinfo.objects.all()
    return render(request, 'test_orm_old/edit_employee_old.html',
                  {'emp': emp, 'dep_list': dep_list, 'group_list': group_list, 'info_list': info_list})


# 正向和反向查找
def test_foreign(request):
    # 取出employee的一条记录
    emp = employee.objects.get(id=28)
    # 正向操作，通过外键值dep关联到department数据表的一条记录，然后取得该记录的dep_name字段
    dep_name = emp.dep.dep_name
    dep_obj = department.objects.get(id=6)
    # 反向操作，通过employee_set关联到employee数据表，然后用all()函数取得其全部记录
    emp_list = dep_obj.employee_set.all()
    emp_names = [emp.name for emp in emp_list]
    return HttpResponse("1.正向关联 <br> 员工名称:{0} <br> 所在部门名称:{1} <br> 2.反向查找 <br> 部门名称:{2} <br>部门员工:{3}".
                        format(emp.name, dep_name, dep_obj.dep_name, emp_names))


# 正向操作查询字段值，取得字段值的形式为“外键+双下划线+关联表的字段名
def test_foreign2(request):
    emp1_tuple = employee.objects.values_list('name', "dep__dep_name", "dep__dep_script")
    print(emp1_tuple)
    emp2_list = employee.objects.values('name', "dep__dep_name", "dep__dep_script")
    print(emp2_list)
    return HttpResponse("emp:{0}<br>emp2:<br>{1}".format(emp1_tuple, emp2_list))


# 反向操作查询字段值，取得字段值的形式为“表名+双下划线+字段名”，表名是有外键字段的表的名称
def test_foreign3(request):
    dep_emp = department.objects.values_list("employee__name")
    print(dep_emp)
    return HttpResponse("emp:{0}".format(dep_emp))


# 多对多键跨表关联操作create()函数
def test_create(request):
    # 反向操作
    group.objects.first().employee_set.create(name='ww', email='578060214@qq.com', dep_id='1', salary='8')
    # 或者
    # group.objects.get(id=2).employee_set.create(name='ww', email='578060214@qq.com', dep_id='1', salary='8')

    # 正向操作
    employee.objects.first().group.create(group_name='搏击', group_script='搏击也是健身项目')


# 多对多键跨表关联操作add()函数
def test_add(request):
    group_list = group.objects.filter(id__lt=6)
    # employee.objects.first().group.add(*group_list)
    # 或
    employee.objects.get(id=31).group.add(*group_list)
    # 或
    # employee.objects.first().group.add(*[1, 2, 6])


# 多对多键跨表关联操作set()函数
def test_set(request):
    # 不管该记录以前关联任何记录，用新的关联替换
    employee.objects.get(id=50).group.set([4, 5, 6])
    # 或
    # employee.objects.first().group.set([4, 5, 6])

# 多对多键跨表关联操作remove()函数
def test_remove(request):
    # 从employee数据表中取出第一条记录，然后删除这条记录关联的group数据表中id值为4的记录
    obj_list = employee.objects.all().first()
    obj_list.group.remove(4)

# 多对多键跨表关联操作clear()函数
def test_clear(request):
    # 从记录对象中删去一切关联记录。以下代码将删去employee数据表中第一条或最后一条记录与group数据表中关联的一切记录
    employee.objects.first().group.clear()
    # employee.objects.last().group.clear()

# 多对多关联跨表正向操作查询字段值
def test_values_list(request):
    emp_m2m_1 = employee.objects.values_list("id", "name", "group__group_name")
    print(emp_m2m_1)

# 多对多关联跨表反向操作查询字段值
def test_value(request):
    emp_m2m_2 = group.objects.values("group_name", "employee__name", "employee__email")
    print(emp_m2m_2)