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


def RandomNumberAdd(request,link,qno):
    randoms = RandomNumber.objects.filter(question_id = qno)
    if len(randoms) == 5:
        return JsonResponse({
            "status": False,
            "msg": "You can not add more than 5 random variables."
        })
    try:
        float(request.POST["min_val"])
        float(request.POST["max_val"])
    except:
        return JsonResponse({
            "status": False,
            "msg": "Please specify valid numbers in min_val and max_val."
        })

    RandomNumber.objects.create(
        question_id = qno,
        min_num = float(request.POST["min_val"]),
        max_num = float(request.POST["max_val"]),
        var_number = len(randoms)+1
    )

    return JsonResponse({
        "status": True,
        "var_num": len(randoms)+1,
        "min_val": request.POST["min_val"],
        "max_val": request.POST["max_val"],
    })