from django.shortcuts import render,redirect
from django.http import HttpResponse
from crud.form import EmployeeForm
from crud.models import Employee

# Create your views here.


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,'home.html',{'form':form})

def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees })

def edit(request,id):
    employee=Employee.objects.get(pk=id)

    return render(request,'edit.html',{'employee':employee})
def update(request,id):
    employee=Employee.objects.get(pk=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'employee':employee}) 

def delete(request,id):
    try:
        employee=Employee.objects.get(pk=id)
        employee.delete()
    except:
        pass
    return redirect('/show')

