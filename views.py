import base64
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

def home(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            employee = form.save(commit=False)

            photo = request.FILES.get('upload_photo')

            if photo:
                employee.photo = photo.read()

            employee.save()
            return redirect('/')

    else:
        form = EmployeeForm()

    employee_data = []

    for emp in employees:
        image = None

        if emp.photo:
            image = base64.b64encode(emp.photo).decode('utf-8')

        employee_data.append({
            'id': emp.id,
            'name': emp.name,
            'dob': emp.dob,
            'photo': image
        })

    return render(request, 'index.html', {
        'form': form,
        'employees': employee_data
    })


def edit_employee(request, id):
    emp = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        emp.name = request.POST['name']
        emp.dob = request.POST['dob']

        if request.FILES.get('upload_photo'):
            emp.photo = request.FILES['upload_photo'].read()

        emp.save()
        return redirect('/')

    return render(request, 'edit.html', {'emp': emp})


def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('/')