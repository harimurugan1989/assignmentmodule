import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student
from django.shortcuts import redirect, render
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def randnumber(a,b):
    return random.randint(a,b)

@login_required
def asummary(request):
    pro=Profile.objects.filter(user=request.user).first()
    if pro.type=='t':
        codes=CreateLink.objects.filter(creator=request.user).all()
        return render(request, "CreateAssignment/safebook.html", {"simple": codes})
