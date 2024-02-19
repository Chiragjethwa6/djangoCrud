from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname' : 'Full Name'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select Position'
        self.fields['fullname'].widget.attrs['class'] = 'form-control'
        self.fields['fullname'].widget.attrs['placeholder'] = 'Enter Full Name'
        self.fields['fullname'].widget.attrs['required'] = 'required'    
        self.fields['empcode'].widget.attrs['class'] = 'form-control'
        self.fields['empcode'].widget.attrs['placeholder'] = 'Enter Employee Code'
        self.fields['empcode'].widget.attrs['required'] = 'required'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['placeholder'] = 'Enter Mobile Number'
        self.fields['mobile'].widget.attrs['required'] = 'required'
        self.fields['position'].widget.attrs['class'] = 'form-control'
        self.fields['position'].widget.attrs['required'] = 'required'
        self.fields['position'].widget.attrs['placeholder'] = 'Select Position'