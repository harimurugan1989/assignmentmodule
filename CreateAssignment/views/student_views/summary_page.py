from django.http import JsonResponse
from CreateAssignment.models import Question, CreateLink, Profile, QueImg,QueText,SubQuestion, StudentRandom, RandomNumber
from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required
import json


def randnumber(a,b):
    return random.randint(a,b)

def create_random (user, question):
    randoms = StudentRandom.objects.filter(question = question).filter(user = user).first()
    if randoms == None:
        randoms = StudentRandom.objects.create(question = question,user = user,randoms = "")
        random_data = RandomNumber.objects.filter(question = question).all()
        re = []
        for i in range(len(random_data)):
            re.append(-1)
        for i in range(len(random_data)):
            if random_data[i].integers_only:
                re[random_data[i].var_number-1] = random.randint(random_data[i].min_num,random_data[i].max_num)
            else:
                re[random_data[i].var_number-1] = round(random.uniform(random_data[i].min_num,random_data[i].max_num),4)
        randoms.randoms = json.dumps(re)
        randoms.save()
    return randoms

                

@login_required
def StudentSummary(request,link):
    user_type = Profile.objects.filter(user = request.user).first().type
    if user_type == 't':
        assignment = CreateLink.objects.filter(link = link).first()
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
                txt = str(subquestion.text)
                for j in range(len(randoms)):
                    txt = txt.replace("<var"+str(j+1)+">",str(randoms[j]))
                subquestion.text = txt
            res.append({
                    "question_data": question,
                    "que": que,
                    "subquestions": subquestions,
                })
        return render(request,"student_assignment/summary.html",{"front":res})
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