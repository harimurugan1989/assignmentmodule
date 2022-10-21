import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def Register(request):
    if request.method == 'POST' :
        register = User()
        if request.POST["college"] == '' or request.POST["roll_no"] == '' or  request.POST["username"]=="" or request.POST["password1"] == ""  or request.POST["password2"]=="":
            messages.error(request,'Please fill all the information!')
            return redirect('./')
        register.username = request.POST["username"].lower()
        register.email = request.POST["email"].lower()
        if request.POST["password1"]==request.POST["password2"]:
            register.set_password(request.POST["password1"])
            register.save()
            pro=Profile()
            y = User.objects.filter(username = request.POST["username"].lower()).first()
            pro.user_id=y.id
            pro.roll_no = request.POST["roll_no"]
            pro.college = request.POST["college"]
            pro.type = request.POST["role"]
            pro.save()
            messages.success(request,"Registered successfully as "+request.POST["username"].lower())
            return redirect('./')
        else:
            messages.error(request,"Passwords did not match")
            return redirect('./')
    return render(request,'CreateAssignment/register.html')
        