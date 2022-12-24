import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, QueText
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def QuestionAdd(request,link):
    assignment = CreateLink.objects.filter(link = link).first()
    question = Question.objects.create(assignment = assignment)
    text = QueText.objects.create(question = question , text = '')
    return redirect('../edit_question/'+str(question.id))
    # return render(request,"CreateAssignment/questions.html")
   