from django.http import JsonResponse
from CreateAssignment.models import Question, CreateLink, Profile, QueImg,QueText,SubQuestion
from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required
import json


def randnumber(a,b):
    return random.randint(a,b)


@login_required
def StudentSummary(request,link):
    user_type = Profile.objects.filter(user = request.user).first().type
    if user_type == 't':
        questions_id = CreateLink.objects.filter(link = link).first().id
        questions = Question.objects.filter(assignment_id = questions_id).all()
        res = []
        for question in questions:  
            arr = ""
            it = question.order
            for i in json.loads(it):
                if(i["type"] == 't'):
                    arr+= str(QueText.objects.filter(id = i["id"]).first().text)+"<br>"
                else:
                    arr+="<img height = \'100px\' src=\'./../../../../../media/"+str(QueImg.objects.filter(id = i["id"]).first().image)+"\'> <br>"
            res.append({"que": arr,"id":question.id,"subquestions": SubQuestion.objects.filter(question_id = question.id).all()})
        return render(request,"student_assignment/summary.html",{"front":res})
    else:
        return JsonResponse({"status":"not doing"})