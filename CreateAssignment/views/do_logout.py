import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def DoLogout(request):
    logout(request)
    return render(request,'CreateAssignment/logout.html')