from CreateAssignment.models import Question, CreateLink, StudentAnswer as Student
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def TakeAssignment(request,link):
    codes_id=CreateLink.objects.filter(link=link).first()
    content=[]
    dic={}
    ques = Question.objects.filter(assignment_id=codes_id.id).all()
    num= 1
    for questiondatas in ques:
        questions={}
        data=Student.objects.filter(username=request.user,link_id=codes_id.id,qno_id=questiondatas.id).first()
        j=1
        i='$'+str(j)
        k=0
        while(questiondatas.question.find(i)!=-1):
            questiondatas.question=questiondatas.question.replace(i,str(data.R[k]))
            k+=1
            j+=1
            i='$'+str(j)
        questions["question"]=questiondatas.question
        questions["explanation"]=questiondatas.explanation
        questions["ques_num"]=num
        content.append(questions)
        num+=1
    dic={"questions":content}
    return render(request,'CreateAssignment/assignment.html',{"content":dic})
    
