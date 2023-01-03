from django.http import JsonResponse
from CreateAssignment.models import *
from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required
import json
# from CreateAssignment.views import create_student_score,create_random,create_student_answer

from .random_create import create_random
from .answers_create import create_student_answer
from .score_create import create_student_score


def randnumber(a,b):
    return random.randint(a,b)





                

@login_required
def StudentSummary(request,link):
    user_type = Profile.objects.filter(user = request.user).first().type
    if user_type == 't':
        assignment = CreateLink.objects.filter(link = link).first()
        score = create_student_score(request.user,assignment).score
        questions_id = assignment.id
        questions = Question.objects.filter(assignment_id = questions_id).all()
        res = []
        for question in questions: 
            randoms = json.loads(create_random(request.user,question).randoms)
            que = []
            it = question.order
            for i in json.loads(it):
                if(i["type"] == 't'):
                    txt = str(QueText.objects.filter(id = i["id"]).first().text)
                    for j in range(len(randoms)):
                        txt = txt.replace("<var"+str(j+1)+">",str(randoms[j]))
                    que.append({ 
                        "type" : "t",
                        "text": txt
                    })
                else:
                    que.append({ 
                        "type" : "i",
                        "url" : "./../../../../../media/"+str(QueImg.objects.filter(id = i["id"]).first().image),
                    })
            subquestions = SubQuestion.objects.filter(question_id = question.id).all()
            for subquestion in subquestions:
                subquestion.correct = create_student_answer(request.user,subquestion,assignment).answer
                txt = str(subquestion.text)
                for j in range(len(randoms)):
                    txt = txt.replace("<var"+str(j+1)+">",str(randoms[j]))
                subquestion.text = txt
            res.append({
                    "question_data": question,
                    "que": que,
                    "subquestions": subquestions,
                })
        return render(request,"student_assignment/summary.html",{"front":res,"score":score})
    else:
        return JsonResponse({"status":"not doing"})

        '''

        que =  [
            {
                que_data: {},
                subquestions: [
                    {   
                        type: t/s,
                        subquestion_data: {},                        
                    }
                ]
            }
        ]


        '''