from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model = User
        fields=['username','email','password1','password2']

    

class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()

    class Meta:
        model = User
        fields=['username','email']


class UserDetailForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['roll_no','college','type']

 
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input  

