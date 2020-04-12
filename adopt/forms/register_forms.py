from django import forms
from adopt.models.register_model import user_detail
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta():
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
        fields = ('username','email','password')


class registerform(forms.ModelForm):

    class Meta():
        model = user_detail
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'gender': forms.TextInput(attrs={'placeholder': 'Gender'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
        }
        fields = ('name','gender','phone')
