from CreateAssignment.models import Question, QueText
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