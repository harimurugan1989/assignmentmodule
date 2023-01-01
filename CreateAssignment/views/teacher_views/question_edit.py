from CreateAssignment.models import Question,QueImg,QueText, RandomNumber
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from CreateAssignment.models.subquestions import SubQuestion
import json


@login_required
def QuestionEdit(request,link,qno):
    subquestions = SubQuestion.objects.filter(question_id = qno).all()
    arr = []
    it = Question.objects.filter(id = qno).first().order
    for i in json.loads(it):
        if(i["type"] == 't'):
            arr.append("<textarea class = \'que\' name =\'question\' >"+ str(QueText.objects.filter(id = i["id"]).first().text)+"</textarea> <input type ='button' onclick = delete_it("+str(i["id"])+",1) value = 'DELETE' >")
        else:
            arr.append("<img height = \'100px\' src=\'./../../../../../media/"+str(QueImg.objects.filter(id = i["id"]).first().image)+"\'> <input type ='button' onclick = delete_it("+str(i["id"])+",2) value = 'DELETE' >")
    # print(arr)
    randoms = RandomNumber.objects.filter(question_id = qno).all()

    return render(
        request,
        "CreateAssignment/edit_question.html",
        {
            "subquestions":subquestions,
            "questions": arr,
            "randoms": randoms,
        }
    )



'''
[
    {
        "type" : t/i,
        "id" : ,
    },   
]
'''