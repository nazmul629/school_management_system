from django import forms
from .models import StudentInfo 

class AdmissionStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo 
        fields = '__all__'