from django.http import JsonResponse
from CreateAssignment.models import SubQuestion


def SubQuestionAdd(request,link,qno):
    try:
        if len(SubQuestion.objects.filter(question_id = qno).all()) > 40:
            return JsonResponse({"status":False,"msg":"You cannot add more than 5 subquestions for one question"})
        subquestion = SubQuestion.objects.create(
            question_id = qno,
            text = '',
            answer = '',
            explanation = '',
            score = 1
        )
        return JsonResponse({"status" : True,"id":subquestion.id})
    except:
        return JsonResponse({"status": False,"msg":"Some technical issue"})
