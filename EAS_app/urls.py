"""Employee Attendance System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import hod_views, manager_views, employee_views, views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("get_attendance", views.get_attendance, name='get_attendance'),
    path("firebase-messaging-sw.js", views.showFirebaseJS, name='showFirebaseJS'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),
    path("admin/home/", hod_views.admin_home, name='admin_home'),
    path("manager/add", hod_views.add_manager, name='add_manager'),
    path("department/add", hod_views.add_department, name='add_department'),
    path("send_employee_notification/", hod_views.send_employee_notification,name='send_employee_notification'),
    path("send_manager_notification/", hod_views.send_manager_notification,name='send_manager_notification'),
    path("add_contract/", hod_views.add_contract, name='add_contract'),
    path("admin_notify_employee", hod_views.admin_notify_employee,name='admin_notify_employee'),
    path("admin_notify_manager", hod_views.admin_notify_manager,name='admin_notify_manager'),
    path("admin_view_profile", hod_views.admin_view_profile,name='admin_view_profile'),
    path("check_email_availability", hod_views.check_email_availability,name="check_email_availability"),
    path("contract/manage/", hod_views.manage_contract, name='manage_contract'),
    path("contract/edit/<int:contract_id>",hod_views.edit_contract, name='edit_contract'),
    path("employee/view/feedback/", hod_views.employee_feedback_message,name="employee_feedback_message",),
    path("manager/view/feedback/", hod_views.manager_feedback_message,name="manager_feedback_message",),
    path("employee/view/leave/", hod_views.view_employee_leave,name="view_employee_leave",),
    path("manager/view/leave/", hod_views.view_manager_leave, name="view_manager_leave",),
    path("attendance/view/", hod_views.admin_view_attendance,name="admin_view_attendance",),
    path("attendance/fetch/", hod_views.get_admin_attendance,name='get_admin_attendance'),
    path("employee/add/", hod_views.add_employee, name='add_employee'),
    path("section/add/", hod_views.add_section, name='add_section'),
    path("manager/manage/", hod_views.manage_manager, name='manage_manager'),
    path("employee/manage/", hod_views.manage_employee, name='manage_employee'),
    path("department/manage/", hod_views.manage_department, name='manage_department'),
    path("section/manage/", hod_views.manage_section, name='manage_section'),
    path("manager/edit/<int:manager_id>", hod_views.edit_manager, name='edit_manager'),
    path("employee/edit/<int:employee_id>",hod_views.edit_employee, name='edit_employee'),
    path("department/edit/<int:department_id>",hod_views.edit_department, name='edit_department'),
    path("section/edit/<int:section_id>",hod_views.edit_section, name='edit_section'),
    
    
    # Manager
    path("manager/home/", manager_views.manager_home, name='manager_home'),
    path("manager/apply/leave/", manager_views.manager_apply_leave,name='manager_apply_leave'),
    path("manager/feedback/", manager_views.manager_feedback, name='manager_feedback'),
    path("manager/view/profile/", manager_views.manager_view_profile,name='manager_view_profile'),
    path("manager/attendance/take/", manager_views.manager_take_attendance,name='manager_take_attendance'),
    path("manager/attendance/update/", manager_views.manager_update_attendance,name='manager_update_attendance'),
    path("manager/get_employees/", manager_views.get_employees, name='get_employees'),
    path("manager/attendance/fetch/", manager_views.get_employee_attendance,name='get_employee_attendance'),
    path("manager/attendance/save/", manager_views.save_attendance, name='save_attendance'),
    path("manager/attendance/update/", manager_views.update_attendance,name='update_attendance'),
    path("manager/fcmtoken/", manager_views.manager_fcmtoken, name='manager_fcmtoken'),
    path("manager/view/notification/", manager_views.manager_view_notification,name="manager_view_notification"),
    #path("manager/result/add/", manager_views.manager_add_result, name='manager_add_result'),
    #path("manager/result/edit/", EditResultView.as_view(),name='edit_manager_result'),
    #path('manager/result/fetch/', manager_views.fetch_smanager_result,name='fetch_manager_result'),



    # Employee
    path("employee/home/", employee_views.employee_home, name='employee_home'),
    path("employee/view/attendance/", employee_views.employee_view_attendance,name='employee_view_attendance'),
    path("employee/apply/leave/", employee_views.employee_apply_leave,name='employee_apply_leave'),
    path("employee/feedback/", employee_views.employee_feedback,name='employee_feedback'),
    path("employee/view/profile/", employee_views.employee_view_profile,name='employee_view_profile'),
    path("employee/fcmtoken/", employee_views.employee_fcmtoken,name='employee_fcmtoken'),
    path("employee/view/notification/", employee_views.employee_view_notification,name="employee_view_notification"),
    #path('employee/view/result/', employee_views.employee_view_result,name='employee_view_result'),

]
