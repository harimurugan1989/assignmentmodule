from re import sub
from django.http import JsonResponse
from CreateAssignment.models import Question, SubQuestion, question
import json


def SubQuestionSave(request,link,qno):
    print(request.POST)
    # try:
    if request.method == 'POST':
        data = json.loads(request.POST["data"])
        print(data)
        print(data["subquestions"])
        for i in data["subquestions"]:
            sq = SubQuestion.objects.filter(id = i["id"]).first()
            sq.text = i["text"]
            sq.answer = i["answer"]
            sq.explanation = i["explanation"]
            sq.score = int(i["score"])
            sq.save()
        print(data["question"])
        que = Question.objects.filter(id = qno).first()
        que.text = data["question"]
        que.save()

    return JsonResponse({"status" : True})
    # except:
    #     return JsonResponse({"status": False,"msg":"Some technical issue"})
