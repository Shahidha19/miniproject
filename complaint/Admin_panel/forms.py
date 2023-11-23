from django import forms
from django.contrib.auth.models import User
#from .models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import Complaint

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']
'''class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['register_number', 'username', 'department', 'email', 'password']'''
'''class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'department', 'complaint']'''