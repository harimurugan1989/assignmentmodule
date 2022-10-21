import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def QuestionEdit(request,link,qno):
    codes_id=CreateLink.objects.filter(link=link).first()
    ques = Question.objects.filter(assignment_id=codes_id.id).all()
    id_first=ques.values_list('id',flat=True).first()
    change = Question.objects.filter(id=id_first+qno-1).first()
    if request.method == "POST":
        change.question = request.POST["question"]
        change.rand_variable_min=request.POST["rand_variable_min"]
        change.rand_variable_max=request.POST["rand_variable_max"]
        change.explanation = request.POST["explanation"]
        change.save()
        messages.success(request,f"Question has been updated successfully!")
        return redirect("../../")    
    return render(request,"CreateAssignment/edit_question.html",{"questions":change})
