import datetime 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from CreateAssignment.models import Question, CreateLink, Instruction, Profile, Student
from django.shortcuts import redirect, render
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def randlink():
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    for i in alphabets:
        letters.append(i)
    link ='' 
    for i in range(10):
        link += letters[random.randint(0,25)]
        if i==2 or i == 6 :
            link+='-'
    return link


@login_required
def LinkCreate(request):
    pro=Profile.objects.filter(user=request.user).first()
    if pro is None:
        return redirect('login/')
    elif pro.type=='t':
        if request.method == "POST":
            if request.POST["course_name"].strip() == "" or request.POST["assignment_name"].strip() == "" or request.POST["result_time"] == "" or request.POST["start"] =="":
                messages.error(request,"Fill all the details to continue!")
                return redirect("./")

            start = request.POST["start"].replace('T',' ')
            first_sub_time = request.POST["first_sub_time"].replace('T',' ')
            second_sub_time = request.POST["second_sub_time"].replace('T',' ')
            result_time = request.POST["result_time"].replace('T',' ')
            ajf =str(datetime.datetime.strptime(first_sub_time, '%Y-%m-%d %H:%M')-datetime.datetime.strptime(start, '%Y-%m-%d %H:%M'))
            if ajf[0] == '-' or ajf == '0:00:00':
                messages.error(request,'Start time cannot be same or greater than first submission time')
                return redirect('./')
            if str(datetime.datetime.strptime(second_sub_time, '%Y-%m-%d %H:%M')-datetime.datetime.strptime(first_sub_time, '%Y-%m-%d %H:%M'))[0] == '-':
                messages.error(request,'First submission time cannot be same or greater than second submission time')
                return redirect('./')
            if str(datetime.datetime.strptime(result_time, '%Y-%m-%d %H:%M')-datetime.datetime.strptime(second_sub_time, '%Y-%m-%d %H:%M'))[0] == '-':
                messages.error(request,'Second submission time cannot be greater than result time')
                return redirect('./')

            if (datetime.datetime.strptime(start, '%Y-%m-%d %H:%M') <= datetime.datetime.now()):
                messages.error(request,'Start time has to be in future')
                return redirect('./')

            create = CreateLink()
            create.course_name = request.POST["course_name"].strip().replace(" ","-")
            create.assignment_name = request.POST["assignment_name"].strip().replace(" ","-")
            create.start = request.POST["start"]
            create.first_sub_time = request.POST["first_sub_time"]
            create.extend = request.POST["extend"]
            create.second_sub_time = request.POST["second_sub_time"]
            create.no_of_submissions = request.POST["no_of_submissions"]
            create.perc_penalty = request.POST["perc_penalty"]
            create.notif = request.POST["notif"]  
            create.face_rec = request.POST["face_rec"] 
            create.neg_mark = request.POST["neg_mark"]
            create.res_anno= request.POST["res_anno"]
            create.creator_id = request.user.id
            create.result_time = request.POST["result_time"]
            link = None
            while(True):
                link = randlink()
                if CreateLink.objects.filter(link= link).first() is None:
                    break
            create.link= link
            create.save()
            Instruction.objects.create(instructions= "", assignment_id = create.id )
            messages.success(request,f"Assignment has been created successfully!")
            return redirect("../"+link+"/")
        return render(request,"CreateAssignment/home.html")
    elif pro.type =='s':
        return render(request,'CreateAssignment/something.html',{'msg':"Student profile is not permitted to create Assignment"})

