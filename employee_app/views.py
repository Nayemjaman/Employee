from django.shortcuts import render
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
    return render(request, 'add_emp.html')

def remove_emp(request):
    return render(request, 'remove_emp.html')
    
def filter_emp(request):
    return render(request, 'filter_emp.html')
