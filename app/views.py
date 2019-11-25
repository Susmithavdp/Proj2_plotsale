from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Plot_details, Appartment_details, Employees_list, user_list
from django.contrib.auth.decorators import login_required


# Create your views here.
def index_page(request):
    return render(request, 'index.html')


def admin_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    if user:
        login(request, user)
        for x, y in request.session.items():
            print(x + "---" + y)
        return render(request, 'welcome_admin.html')
    else:
        return render(request, 'index.html', {'error_msg': 'Invalid_User'})


def admin_logout(request):
    logout(request)
    return redirect('/')

@login_required()
def add_plot(request):
    return render(request, 'add_plot.html')

@login_required()
def edit_plot(request):
    return render(request, 'edit_plot.html')

@login_required()
def view_plots(request):
    res=Plot_details.objects.all()
    return render(request, 'view_plots.html',{'data':res})

@login_required()
def add_appartment(request):

    return render(request, 'add_appartment.html')

@login_required()
def edit_appartment(request):
    return render(request, 'edit_appartment.html')

@login_required()
def view_appartments(request):
    res=Appartment_details.objects.all()
    return render(request, 'view_appartments.html',{'data':res})

@login_required()
def save_plot_details(request):
    plot_no = request.POST['plot_no']
    road_no = request.POST['road_no']
    survey_no = request.POST['survey_no']
    sq_yards = request.POST['sq_yards']
    cost_per_sq_yard = request.POST['cost_per_sq_yard']
    other_expansis = request.POST['other_expansis']
    boundaries = request.POST['boundaries']
    facing = request.POST['facing']
    total = request.POST['total']
    img = request.POST['img']
    Plot_details(platno=plot_no, roadno=road_no, survey_no=survey_no, sq_yards=sq_yards,
                 cost_per_sq_yard=cost_per_sq_yard, other_expences=other_expansis, boundaries=boundaries, facing=facing,
                 total_cost=total, status="Vecent", plot_image=img).save()
    return render(request, 'add_plot.html', {'msg': "Plot Added Sucessfully"})

@login_required()
def save_appartment_details(request):
    aprt_name = request.POST['aprt_name']
    aprt_add = request.POST['aprt_add']
    aprt_no = request.POST['aprt_no']
    survey_no = request.POST['survey_no']
    bhk = request.POST['bhk']
    cost_per_bhk = request.POST['cost_per_bhk']
    other_expences = request.POST['other_expences']
    facing = request.POST['facing']
    total = request.POST['total']
    img = request.FILES['img']
    Appartment_details(aprt_name=aprt_name, aprt_add=aprt_add, survey_no=survey_no, aprt_no=aprt_no,
                       cost_per_bhk=cost_per_bhk, bhk=bhk, other_expences=other_expences, facing=facing,
                       total_cost=total, status='Vecent', aprt_img=img).save()
    return render(request, 'add_appartment.html', {'msg': "Appartment Added Sucessfully"})

@login_required()
def add_employee(request):
    return render(request, 'add_employee.html')


def save_employee_details(request):
    emp_name = request.POST['emp_name']
    emp_emailid = request.POST['emp_emailid']
    emp_mblno = request.POST['emp_mblno']
    emp_salary = request.POST['salary']
    emp_designation = request.POST['designation']
    emp_work_location = request.POST['emp_work_location']
    emp_remarks = request.POST['emp_remarks']
    Employees_list(emp_id=1001, emp_name=emp_name, emp_emailid=emp_emailid, emp_mblno=emp_mblno, emp_salary=emp_salary,
                   emp_designation=emp_designation, emp_work_location=emp_work_location, emp_remarks=emp_remarks).save()

    return render(request, 'add_employee.html', {'msg': "Employee Added Sucessfully"})

@login_required()
def home_page(request):
    return render(request,'welcome_admin.html')

@login_required()
def create_user(request):
    return render(request,'create_user.html')

@login_required()
def save_user_details(request):
    user_name=request.POST['user_name']
    user_emailid=request.POST['user_emailid']
    user_mblno=request.POST['user_mblno']
    user_addres=request.POST['user_addres']
    user_list(user_name=user_name,user_emailid=user_emailid,user_mblno=user_mblno,user_addres=user_addres,user_id=10003).save()

    return render(request,'create_user.html',{'msg':"User Created Succesfully"})

@login_required()
def viewall_users(request):
    res=user_list.objects.all()
    print(res)
    return render(request,'viewall_users.html',{'data':res})

@login_required()
def open_ed_userpage(request):
    res=user_list.objects.all()

    return render(request,'open_ed_userpage.html',{'data':res})

@login_required()
def edit_user(request):
    user_id=request.GET.get('user_id')
    res=user_list.objects.get(user_id=user_id)
    return render(request,'create_user.html',{'data':res})

@login_required()
def delete_user(request):
    user_id=request.GET.get('user_id')
    user_list.objects.get(user_id=user_id).delete()
    return redirect('viewall_users')

@login_required()
def update_user_details(request):
    user_id=request.POST['user_id']
    user_name = request.POST['user_name']
    user_emailid = request.POST['user_emailid']
    user_mblno = request.POST['user_mblno']
    user_addres = request.POST['user_addres']
    res=user_list.objects.get(user_id=user_id)
    res.user_name=user_name
    res.user_emailid=user_emailid
    res.user_mblno=user_mblno
    res.user_addres=user_addres
    res.save()
    return redirect('viewall_users')

@login_required()
def view_all_employees(request):
    res=Employees_list.objects.all()
    return render(request,'view_all_employees.html',{'data':res})

@login_required()
def open_ed_employeepage(request):
    res=Employees_list.objects.all()
    return render(request,'open_ed_employeepage.html',{'data':res})

@login_required()
def delete_employee(request):
    emp_id = request.GET.get('emp_id')
    Employees_list.objects.get(emp_id=emp_id).delete()
    return redirect('view_all_employees')

@login_required()
def edit_employee(request):
    emp_id = request.GET.get('emp_id')
    res=Employees_list.objects.get(emp_id=emp_id)
    return render(request,'add_employee.html',{'data':res})

@login_required()
def update_employee_details(request):
    emp_id = request.POST.get('emp_id')
    emp_name = request.POST['emp_name']
    emp_emailid = request.POST['emp_emailid']
    emp_mblno = request.POST['emp_mblno']
    emp_salary = request.POST['salary']
    emp_designation = request.POST['designation']
    emp_work_location = request.POST['emp_work_location']
    emp_remarks = request.POST['emp_remarks']
    res=Employees_list.objects.get(emp_id=emp_id)
    res.emp_name=emp_name
    res.emp_emailid=emp_emailid
    res.emp_mblno=emp_mblno
    res.emp_salary=emp_salary
    res.emp_work_location=emp_work_location
    res.emp_remarks=emp_remarks
    res.save()
    return redirect('view_all_employees')

@login_required()
def aprt_details(request):
    aprt_no=request.GET.get('aprt_no')
    res=Appartment_details.objects.get(aprt_no=aprt_no)
    return render(request,'aprt_details.html',{'data':res})

@login_required()
def plot_details(request):
    plotno = request.GET.get('plotno')
    res=Plot_details.objects.get(platno=plotno)
    return render(request,'plot_details.html',{'data':res})
