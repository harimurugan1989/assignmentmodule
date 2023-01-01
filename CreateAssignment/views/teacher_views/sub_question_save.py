from re import sub
from django.http import JsonResponse
from CreateAssignment.models import Question, SubQuestion, question, QueText
import json


def SubQuestionSave(request,link,qno):
    if request.method == 'POST':
        data = json.loads(request.POST["data"])
        for i in data["subquestions"]:
            sq = SubQuestion.objects.filter(id = i["id"]).first()
            sq.text = i["text"]
            sq.answer = i["answer"]
            sq.explanation = i["explanation"]
            sq.score = int(i["score"])
            sq.save()
        que = Question.objects.filter(id = qno).first()
        i,j = 0,0
        for each in json.loads(que.order):
            if each["type"] == 't':
                obj = QueText.objects.filter(id = each["id"]).first()
                obj.text = data["boxes"][j]
                obj.save()
                j+=1
        que.text = data["question"]
        que.save()

    return JsonResponse({"status" : True})
