from django import forms
from .models import Year,Month,Select_Month

class Add_month_form(forms.ModelForm):
    class Meta:
        model = Select_Month 
        fields = '__all__'