"""Proj2_flotsale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Proj2_plotsale import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_page),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('add_plot/',views.add_plot,name='add_plot'),
    path('edit_plot/', views.edit_plot, name='edit_plot'),
    path('view_plots/', views.view_plots, name='view_plots'),
    path('add_appartment/', views.add_appartment, name='add_appartment'),
    path('edit_appartment/', views.edit_appartment, name='edit_appartment'),
    path('view_appartments/', views.view_appartments, name='view_appartments'),
    path('save_plot_details/',views.save_plot_details,name='save_plot_details'),
    path('save_appartment_details/',views.save_appartment_details,name='save_appartment_details'),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('save_employee_details/',views.save_employee_details,name='save_employee_details'),
    path('home_page/',views.home_page,name='home_page'),
    path('create_user/',views.create_user,name='create_user'),
    path('save_user_details/', views.save_user_details, name='save_user_details'),
    path('viewall_users/',views.viewall_users,name='viewall_users'),
    path('open_e/d_userpage/',views.open_ed_userpage,name='open_e/d_userpage'),
    path('edit_user/',views.edit_user,name='edit_user'),
    path('delete_user/',views.delete_user,name='delete_user'),
    path('update_user_details/',views.update_user_details,name='update_user_details'),
    path('view_all_employees/',views.view_all_employees,name='view_all_employees'),
    path('open_e/d_employeepage/',views.open_ed_employeepage,name='open_ed_employeepage'),
    path('edit_employee/',views.edit_employee,name='edit_employee'),
    path('delete_user/',views.delete_employee,name='delete_employee'),
    path('update_employee_details/',views.update_employee_details,name='update_employee_details'),
    path('aprt_details/',views.aprt_details,name='aprt_details'),
    path('plot_details/', views.plot_details, name='plot_details'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
