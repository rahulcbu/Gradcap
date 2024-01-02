from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee

# Create your views here.


def employees_index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', context={"employees": employees})
