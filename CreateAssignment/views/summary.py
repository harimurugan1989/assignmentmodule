from django.http import JsonResponse
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student, QueImg,QueText
from django.shortcuts import redirect, render
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json


def randnumber(a,b):
    return random.randint(a,b)

@login_required
def Summary(request,link):
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
            res.append({"que": arr,"id":question.id})
        return render(request,"CreateAssignment/summary.html",{"front":res})
    else:
        return JsonResponse({"status":"not doing"})

# @login_required
# def Summary(request,link):
#     pro=Profile.objects.filter(user=request.user).first()
#     if pro.type=='t':
#         codes_id=CreateLink.objects.filter(link=link).first()
#         content=[]
#         dic={}
#         ques = Question.objects.filter(assignment_id=codes_id.id).all()
#         num= 1
#         for questiondatas in ques:
#             questions={}
#             questions["question"]=questiondatas.question
#             questions["explanation"]=questiondatas.explanation
#             questions["ques_num"]=num
#             content.append(questions)
#             num+=1
#         dic={"questions":reversed(content)}
#         return render(request, "CreateAssignment/summary.html", {"assign": codes_id,"content":dic})
#     elif pro.type=='s':
#         code = CreateLink.objects.filter(link=link).first()
#         inst = Instruction.objects.filter(assignment_id = code.id).first()
#         instructions = inst.instructions.split('\n')
#         num_of_ques = Question.objects.filter(assignment_id=code.id).count()
#         nos=Student.objects.filter(username=request.user,link_id=code.id).count()
#         ques_all=Question.objects.filter(assignment_id=code.id).all()
#         data_m=Student.objects.filter(username=request.user,link_id=code.id,qno=nos+1).first()
#         j=0
#         while(nos<num_of_ques):
#             ques=ques_all[j]
#             if data_m is None:
#                 data=Student()       
#                 rand_arr=[]
#                 data.username=request.user
#                 data.link_id = code.id
#                 data.qno_id=ques.id
#                 r=1
#                 i='$'+str(r)
#                 while(ques.question.find(i)!=-1):
#                     x=randnumber(int(ques.rand_variable_min),int(ques.rand_variable_max))
#                     rand_arr.append(x)
#                     r+=1
#                     i='$'+str(r)
#                 data.R=rand_arr
#                 data.save()
#                 nos+=1
#                 j+=1
#         return render(request,"CreateAssignment/stu_instructions.html",{"lines" : instructions,"assign": code,"noq":num_of_ques })
