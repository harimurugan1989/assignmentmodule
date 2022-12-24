import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, QueText, QueImg
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json


def QuestionAddImage(request,link,qno):
    img_box = QueImg.objects.create(question_id = qno,image = request.FILES["img"])
    print(img_box.id)
    question = Question.objects.filter(id = qno).first()
    order = json.loads(question.order)
    order.append({
        "type": "i",
        "id": img_box.id
    })
    question.order = json.dumps(order)
    question.save()
    return JsonResponse({
        "status": True,
        "id": img_box.id,
        "address": str(img_box.image) 
    })



