import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, QueText
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json


def QuestionAddTextbox(request,link,qno):
    text_box = QueText.objects.create(question_id = qno,text = "")
    question = Question.objects.filter(id = qno).first()
    order = json.loads(question.order)
    order.append({
        "type": "t",
        "id": text_box.id
    })
    question.order = json.dumps(order)
    question.save()
    return JsonResponse({
        "status": True,
        "id": text_box.id
    })