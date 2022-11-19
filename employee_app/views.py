from datetime import datetime
from django.shortcuts import render,HttpResponse
from .models import Employee
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')
def all_emp(request):
    all_amployee = Employee.objects.all()
    context = {
        'all_amployee': all_amployee
    }
    return render(request, "all_emp.html",context)
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone_number = request.POST['phone_number']
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone_number=phone_number,dept_id=dept,role_id=role,hire_date=datetime.now())
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
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        all_amployee = Employee.objects.all()
        if name:
            all_amployee = all_amployee.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            all_amployee = all_amployee.filter(dept__name__icontains = dept)
        if role:
            all_amployee = all_amployee.filter(role__name__icontains = role)

        return render(request, 'all_emp.html', {'all_amployee': all_amployee})

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
