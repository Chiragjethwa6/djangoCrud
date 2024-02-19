from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request):
    data = {'employees':Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', data)

def employee_form(request, id=0):
    if request.method == 'POST':
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    else:
        if id == 0:
            employee = Employee()
        else:
            employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form':form})


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
