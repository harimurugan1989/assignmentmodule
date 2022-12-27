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


def RandomNumberDelete(request,link,qno):
    var_num = int(request.POST["var_num"])
    print(var_num)
    randoms = RandomNumber.objects.filter(question_id = qno).all()
    for each in randoms:
        if each.var_number == var_num:
            each.delete()
    for each in randoms:
        if each.var_number > var_num:
            each.var_number -= 1
            each.save()
    return JsonResponse({
        "status": True,
    })