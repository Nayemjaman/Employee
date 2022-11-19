from datetime import datetime
from django.shortcuts import render,HttpResponse
from .models import Employee,Depertment,Role

# Create your views here.

def index(request):
    return render(request, 'index.html')
def all_emp(request):
    all_employee = Employee.objects.all()
    context = {
        'all_employee': all_employee
    }
    return render(request, "all_emp.html",context)
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bouns = int(request.POST['bouns'])
        phone_number = request.POST['phone_number']
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bouns=bouns,phone_number=phone_number,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Added successfuly')
    else:
        return render(request, 'add_emp.html')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            remove_emp = Employee.objects.get(id=emp_id)
            remove_emp.delete()
            return HttpResponse('Deleted.')
        except:
            return HttpResponse('Please give a valid id of employee.')
    all_employee = Employee.objects.all()
    context = {
        'all_employee': all_employee
    }
    return render(request, 'remove_emp.html',context)
    
def filter_emp(request):
    return render(request, 'filter_emp.html')
