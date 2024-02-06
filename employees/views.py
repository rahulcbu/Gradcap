from django.shortcuts import render
from .models import Student

def employees_index(request):
    students = Student.objects.all()
    return render(request, 'employees/index.html', {'students': students})
