import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from CreateAssignment.models.subquestions import SubQuestion

@login_required
def QuestionEdit(request,link,qno):
    subquestions = SubQuestion.objects.filter(question_id = qno).all()
    return render(
        request,
        "CreateAssignment/edit_question.html",
        {
            "subquestions":subquestions,
            "question":Question.objects.filter(id = qno).first().text
        }
    )
