import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def QuestionAdd(request,link):
    pro=Profile.objects.filter(user=request.user).first()
    ques = Question()
    if request.method == "POST":
        ques.assignment_id = CreateLink.objects.filter(link =link).first().id
        ques.question = request.POST["question"]
        ques.rand_variable_min=request.POST["rand_variable_min"]
        ques.rand_variable_max=request.POST["rand_variable_max"]
        ques.explanation = request.POST["explanation"]
        ques.save()
        messages.success(request,f"Question has been added successfully!")
        return redirect("../")
    return render(request,"CreateAssignment/questions.html")
   