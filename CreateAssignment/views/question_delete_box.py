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
import os
from backend import settings


def QuestionDeleteBox(request,link,qno):
    cmp = "t" if int(request.POST["type"]) == 1 else "i"

    question = Question.objects.filter(id = qno).first()
    order = json.loads(question.order)
    i = 0
    for od in order:
        if od["id"] == int(request.POST["id"]) and od["type"] == cmp:
            order.pop(i)
            break
        i+=1
    question.order = json.dumps(order)
    question.save()
    
    if cmp == "t" : 
        QueText.objects.filter(id = int(request.POST["id"])).delete()
    else :
        print("to mein kya karu ab")
        img = QueImg.objects.filter(id = int(request.POST["id"]))
        img.delete()
    
    return JsonResponse({
        "status": True
    })