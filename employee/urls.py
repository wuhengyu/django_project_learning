# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 19:39
# @Author  : Walter
# @File    : urls.py
# @License : (C)Copyright Walter
# @Desc    :
from django.urls import path
# 导入视图函数，*代表所有
from employee.views import *

urlpatterns = [
    # 操作员工数据表（employee）相关URL配置项
    path('list_employee_old/', list_employee_old),
    path('add_employee_old/', add_employee_old),
    path('edit_employee_old/<int:emp_id>/', edit_employee_old),
    path('del_employee_old/<int:emp_id>/', delete_employee_old),
    # 操作部门数据表（department）相关URL配置项
    path('add_dep_old/', add_dep_old),
    path('list_dep_old/', list_dep_old),
    path('del_dep_old/<int:dep_id>/', del_dep_old),
    path('edit_dep_old/<int:dep_id>/', edit_dep_old),
    # 操作团体数据表（group）相关URL配置项
    path('add_group_old/', add_group_old),
    path('list_group_old/', list_group_old),
    path('del_group_old/<int:group_id>/', del_group_old),
    path('edit_group_old/<int:group_id>/', edit_group_old),
    # 操作员工补充信息数据表（employeeinfo）相关URL配置项
    path('add_employeeinfo_old/', add_employeeinfo_old),
    path('list_employeeinfo_old/', list_employeeinfo_old),
    path('del_employeeinfo_old/<int:info_id>/', del_employeeinfo_old),
    path('edit_employeeinfo_old/<int:info_id>/', edit_employeeinfo_old),

    # 正向操作和反向操作
    path('test_foreign/', test_foreign),
    path('test_foreign2/', test_foreign2),
    path('test_foreign3/', test_foreign3),

    # 多对多键跨表关联操作
    path('test_create/', test_create),
    path('test_add/', test_add),
    path('test_set/', test_set),
    path('test_remove/', test_remove),
    path('test_clear/', test_clear),

    path('test_values_list/', test_values_list),
    path('test_value/', test_value),
]
