from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    upload_photo = forms.ImageField(required=False)

    class Meta:
        model = Employee
        fields = ['name', 'dob', 'upload_photo']