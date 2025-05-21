from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def wish(request, name):
    return render(request,'wish.html',{'name':name})

def get_employees(request):
    all_users = Employee.objects.all()
    return render(request,'get_employees.html',{'all_users':all_users})

def get_emp(request, pk):
    all_users = Employee.objects.get(pk=pk)
    for user in all_users:
        if user.empno == int(pk):
            return render(request,'get_emp.html',{'user':user})
    return HttpResponse('User not found')
# ---or----
#user = Employee.pbjects.get(pk=pk)
#return render(request, 'get_emp.html', {'user': user})