from CreateAssignment.models import Question, QueText, QueImg
from django.http import JsonResponse
import json


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