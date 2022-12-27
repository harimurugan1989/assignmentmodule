import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, QueText, RandomNumber 
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json


def RandomNumberEdit(request,link,qno):
    randoms = RandomNumber.objects.filter(question_id = qno).all()
    print(request.POST)
    print(request.POST["min_vals"])
    print(request.POST["max_vals"])
    mi,ma = request.POST["min_vals"].split(','),request.POST["max_vals"].split(',')
    for i in mi:
        try:
            float(i)
        except:
            return JsonResponse({
            "status": False,
            "msg": "Please specify valid numbers in min_val and max_val."
        })
    for i in ma:
        try:
            float(i)
        except:
            return JsonResponse({
            "status": False,
            "msg": "Please specify valid numbers in min_val and max_val."
        })
    i = 0
    for each in randoms:
        each.min_num = mi[i]
        each.max_num = ma[i]
        i+=1
        each.save()

    return JsonResponse({
        "status": True,
    })