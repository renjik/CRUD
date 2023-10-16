from django.shortcuts import render, redirect

from app1.models import Employee

from app1.forms import EmployeeForm

# Create your views here.
def employees_list(request):

    employees = Employee.objects.all()

    context = {

                'employees': employees,

                }

    return render(request, 'list.html', context)

def create_employee(request):

    form = EmployeeForm()

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('employees-list')

    context = {

    'form': form,

    }

    return render(request, 'create.html', context)

def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    form = EmployeeForm(instance=employee)

    if request.method == 'POST':

        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():

                form.save()

                return redirect('employees-list')

    context = {

        'employee': employee,

        'form': form,

        }
    return render(request, 'edit.html', context)

def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':

        employee.delete()

        return redirect('employees-list')

    context = {

        'employee': employee,

        }

    return render(request, 'delete.html', context)