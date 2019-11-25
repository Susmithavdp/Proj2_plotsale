from django.db import models

# Create your models here.
class Plot_details(models.Model):
    platno=models.IntegerField(unique=True,primary_key=True)
    roadno=models.CharField(max_length=20)
    survey_no=models.CharField(max_length=10)
    sq_yards=models.IntegerField(default=False)
    cost_per_sq_yard=models.IntegerField()
    other_expences=models.IntegerField()
    boundaries=models.CharField(max_length=30)
    facing=models.CharField(max_length=10)
    total_cost=models.IntegerField()
    posted_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=10,default=False)
    plot_image=models.FileField(default=False,upload_to='plot/')
class Appartment_details(models.Model):
    aprt_name=models.CharField(max_length=30)
    aprt_add=models.TextField()
    aprt_no=models.IntegerField(unique=True,primary_key=True)
    survey_no=models.CharField(max_length=10)
    bhk=models.IntegerField()
    cost_per_bhk=models.IntegerField()
    facing=models.CharField(max_length=10)
    other_expences=models.IntegerField()
    total_cost=models.IntegerField()
    posted_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=10,default=False)
    aprt_img=models.FileField(upload_to='')
class Employees_list(models.Model):
    emp_id=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=30)
    emp_emailid=models.EmailField()
    emp_mblno=models.IntegerField()
    emp_salary=models.IntegerField()
    emp_doj=models.DateField(auto_now_add=True)
    emp_designation=models.CharField(max_length=10)
    emp_work_location=models.TextField()
    emp_remarks=models.CharField(max_length=10)
class user_list(models.Model):
    user_id =models.IntegerField(unique=True)
    user_name =models.CharField(max_length=30)
    user_emailid =models.EmailField()
    user_mblno =models.IntegerField()
    user_created_date =models.DateField(auto_now_add=True)
    user_addres =models.TextField()




