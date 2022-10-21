import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def QuestionDelete(request,link,qno):
    if request.method =='POST':
        codes_id=CreateLink.objects.filter(link=link).first()
        ques = Question.objects.filter(assignment_id=codes_id.id).all()
        id_first=ques.values_list('id',flat=True).first()
        Question.objects.filter(id = id_first+qno-1).first().delete()
        messages.success(request,f"Question has been deleted successfully!")
        return redirect('../../')
    return render(request,"CreateAssignment/delete_question.html")
