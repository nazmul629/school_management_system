from django import forms
from django.contrib.auth.models import User

class UsersiginupForms(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class userloginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))