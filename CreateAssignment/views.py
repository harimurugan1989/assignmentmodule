from datetime import datetime 
from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
from django.contrib import messages
from .models import instructions
from .models import createlink
from .models import questiondata
# from .models import assignquestion
from .forms import UserRegisterForm,UserUpdateForm,UserDetailForm
from .models import Profile
# from .models import 
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Profile
from .models import st_data
import os
from .models import *
import datetime

# from .forms import quest
from django.forms import modelformset_factory

from PIL import Image


RANDOM_LINK_GENERATED=''
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
# Create your views here.
@login_required
def linkcreate(request):
    userr=[]
    create=[]
    userr=request.user.username
    if request.method == "POST":
              # print('HELLO WORLD')
        #try:
           # if request.POST["course_name"].strip() == "" or request.POST["assign_name"].strip() == "" or request.POST["result_time"] == "" or request.POST["start"] =="":
               # messages.error(request,"Fill all the details to continue!")
                #return redirect("./")
        #except:
              #  messages.error(request,"Fill all the details to continue!")
               # return redirect("./")
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

        create = createlink()
        create.course_name = request.POST["course_name"].strip().replace(" ","-")
        create.assignment_name = request.POST["assignment_name"].strip().replace(" ","-")
        create.start = request.POST["start"]
        create.first_sub_time = request.POST["first_sub_time"]
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
            if createlink.objects.filter(link= link).first() is None:
                break
        print("link",link)
        create.link= link
        create.save()
        # userr=user.request.id
        instructions.objects.create(instruction="",assignm_id=create.id)
        messages.success(request,f"Assignment has been created successfully!")
        return redirect("/"+link+"/")
        
    return render(request,"CreateAssignment/home_old.html",{"use":userr, "create":create})

@login_required
def summary(request,link):  
    codes_id= createlink.objects.filter(link=link).first()
    everyquestion = questiondata.objects.filter(link_id=codes_id.id).all()
    # print(everyquestion)
    # contents={}
    flist=[]
    
    # # content=everyquestion
    # for each in everyquestion:
    #     contents={}
    #     # print(str(each.photo1))
    #     contents["photo1"]=str(each.photo1)
    #     print(contents)
    #     print(each.id)
    #     flist.append(contents)
    
    # print(flist)
    # for each in everyquestion:
    #     print(each.photo1)
        # contents["photo1"]=str(each.photo1)
        # flist.append(contents)
        # print(flist)       
    # all_sections = []
    # content = []
    # dic = {}
    # if codes_id is not None :
    #    everyquestion = questiondata.objects.filter(link_id=codes_id.id).all()
    #    num = 1
    # #    for questiondatas in everyquestion:
    # #     questions = {}
    # #     options = {} 
    # #     i = 1
    # #     # for type in questiondatas.options.split('/.\\'):
    # #     #     if type == '':
    # #     #         continue
    # #     #     options['opt_'+str(i)] = type 
    # #     #     i += 1
    # #     questions["question"]=questiondatas.question
    # #     questions["type"]= questiondatas.type
    # #     questions["explanation"]=questiondatas.explanation
    # #     questions["ques_num"]=num
    # #     questions["number"]=questiondatas.id
    # #     questions["image"]=str(questiondatas.photo)
    # #     content.append(questions)
    # #     num+=1
    # # else:
    # #     print(codes_id)
    # print(everyquestion)
    # dic = {"questions":reversed(content)}
    # all_sections.append(dic)
    return render(request,"CreateAssignment/summary_page.html",{"questions":everyquestion, "content":flist})
    

@login_required
def instruct(request,link):
    code=createlink.objects.filter(link=link).first()
    inst = instructions.objects.filter(assignm_id=code.id).first()
    if request.method == "POST":
        print(request.POST["instruction"])
        inst.instruction= request.POST["instruction"]
        inst.save()
        messages.success(request,f"Instructions have been updated successfully!")
        return redirect("./")
    return render(request,"CreateAssignment/instructions.html",{"insth":inst.instruction})


@login_required
def settings(request,link):        
    create= createlink.objects.filter(link =link).first()   
    print(create)
    if request.method == 'POST':
        # start = request.POST["start"].replace('T',' ')
        # if request.method
        # start = request.POST["start"].replace('T',' ')
        # margin = request.POST["margin"].replace('T',' ')
        # result = request.POST["result"].replace('T',' ')
        # ajf =str(datetime.strptime(margin, '%Y-%m-%d %H:%M')-datetime.strptime(start, '%Y-%m-%d %H:%M'))
        # if ajf[0] == '-' or ajf == '0:00:00':
        #     messages.error(request,'Last Login time can not be same or greater than the quiz start time')
        #     return redirect('./')
        # if str(datetime.strptime(result, '%Y-%m-%d %H:%M')-datetime.strptime(margin, '%Y-%m-%d %H:%M'))[0] == '-':
        #     messages.error(request,'Result Opening time can not be greater than the Last Login time')
        #     return redirect('./')
        create.course_name = request.POST["course_name"].strip().replace(" ","-")
        create.assignment_name = request.POST["assignment_name"].strip().replace(" ","-")
        create.start = request.POST["start"]
        create.first_sub_time = request.POST["first_sub_time"]
        create.second_sub_time = request.POST["second_sub_time"]
        create.no_of_submissions = request.POST["no_of_submissions"]
        create.perc_penalty = request.POST["perc_penalty"] 
        create.notif = request.POST["notif"] 
        create.face_rec = request.POST["face_rec"] 
        create.neg_mark = request.POST["neg_mark"] 
        create.res_anno= request.POST["res_anno"] 
        create.creator_id = request.user.id
        create.result_time = request.POST["result_time"]
        create.save()
        messages.success(request,"Settings Updated Successfully")
        return redirect('./')
    print(create.start)
    # start_v = str(code.start)[:10]+'T'+str(code.start)[11:16]
    # data = {'course':code.course_name,'start':start_v,"code_id":code.id}
    return render(request,'CreateAssignment/settings.html',{"create":create})


@login_required
def deletelink(request,link):
    if request.method == "POST":
        x = createlink.objects.filter(link = link).all().delete()
        return redirect('CreateAssignment-home')
    return render(request,"CreateAssignment/deletelink.html")


def addquestion(request,link):        
    code=createlink.objects.filter(link=link).first()
    # qno= createlink.objects.filter(link=link).first()
    # print(qno)
    # quesformset=modelformset_factory(assignquestion, fields=('question','marks','ans'), extra=1)
    ques={}
    if request.method == 'POST':
        ques=questiondata()
        # ques=assignquestion()
        # start = request.POST["start"].replace('T',' ')
        # if request.method
        # start = request.POST["start"].replace('T',' ')
        # margin = request.POST["margin"].replace('T',' ')
        # result = request.POST["result"].replace('T',' ')
        # ajf =str(datetime.strptime(margin, '%Y-%m-%d %H:%M')-datetime.strptime(start, '%Y-%m-%d %H:%M'))
        # if ajf[0] == '-' or ajf == '0:00:00':
        #     messages.error(request,'Last Login time can not be same or greater than the quiz start time')
        #     return redirect('./')
        # if str(datetime.strptime(result, '%Y-%m-%d %H:%M')-datetime.strptime(margin, '%Y-%m-%d %H:%M'))[0] == '-':
        #     messages.error(request,'Result Opening time can not be greater than the Last Login time')
        #     return redirect('./')
      
        ques.des1= request.POST["des1"]
        
        try:
            ques.photo1 = request.FILES["photo1"]
        except:
            ct =1
        try:
            ques.rmin1=request.POST["rmin1"]
            ques.rmin2=int(request.POST["rmin2"])
            ques.rmin3=request.POST["rmin3"]
            ques.rmax1=request.POST["rmax1"]
            ques.rmax2=request.POST["rmax2"]
            ques.rmax3=request.POST["rmax3"]
            ques.mark1=request.POST["mark1"] 
        except ValueError:
            ques.rmin1=0
            ques.rmin2=0
            ques.rmin3=0
            ques.rmax1=0
            ques.rmax2=0
            ques.rmax3=0
            ques.mark1=0


        ques.ques1=request.POST["ques1"]
        ques.ans1=request.POST["ans1"]
        ques.exp1=request.POST["exp1"]
        # ques.mark2=request.POST["mark2"] 
        # ques.ques2=request.POST["ques2"]
        # ques.ans2=request.POST["ans2"]
        # ques.exp2=request.POST["exp2"]       
        # ques.mark3=request.POST["mark3"] 
        # ques.ques3=request.POST["ques3"]
        # ques.ans3=request.POST["ans3"]
        # ques.exp3=request.POST["exp3"]       
        try:
            ques.rmax2 = int(ques.rmax2)
        except ValueError:
            ques.rmax2 = 0 
        # ques.mark4=request.POST["mark4"] 
        # ques.ques4=request.POST["ques4"]
        # ques.ans4=request.POST["ans4"]
        # ques.exp4=request.POST["exp4"]       

        # ques.mark5=request.POST["mark5"] 
        # ques.ques5=request.POST["ques5"]
        # ques.ans5=request.POST["ans5"]
        # ques.exp5=request.POST["exp5"]       
        ques.link=code       
        ques.save()
        messages.success(request,"Question added")
        return redirect('./')
    # formset=quesformset(queryset=assignquestion.objects.filter(qno=code.id))
    # code = codes.first()
    # # start_v = str(code.start)[:10]+'T'+str(code.start)[11:16]
    #  data = {'type':code.type,'question':code.question,"explanation":code.explanation}
    # return render(request,'CreateAssignment/new.html',{'formset':formset, "quest":ques})
    return render(request,'CreateAssignment/new.html',{"quest":ques})

def editquestion(request,link,qno):
    # if not ev(request):
    #     return redirect('email-verify')
    code=createlink.objects.filter(link=link).first()
    ques= questiondata.objects.filter(id = qno).first()
    # code = createlink.objects.filter(link = link).first()
    # if code is None:
    #     return render(request,"public/something.html",{'msg':"Check your link again. This Link is not valid.","videos":topThree()})
    # if request.user.id != code.creator_id:
    #     return render(request,"public/something.html",{"msg":"You are not allowed on this page. Please go back.","videos":topThree()})
    # some = {}
    # some["type"] = change.type
    # some["question"] = change.question
    # some["explanation"] = change.explanation
    # some["photo"] = str(change.photo)
    # ques={}
    if request.method == 'POST':
        # ques=questiondata()
        # ques=assignquestion()
        # start = request.POST["start"].replace('T',' ')
        # if request.method
        # start = request.POST["start"].replace('T',' ')
        # margin = request.POST["margin"].replace('T',' ')
        # result = request.POST["result"].replace('T',' ')
        # ajf =str(datetime.strptime(margin, '%Y-%m-%d %H:%M')-datetime.strptime(start, '%Y-%m-%d %H:%M'))
        # if ajf[0] == '-' or ajf == '0:00:00':
        #     messages.error(request,'Last Login time can not be same or greater than the quiz start time')
        #     return redirect('./')
        # if str(datetime.strptime(result, '%Y-%m-%d %H:%M')-datetime.strptime(margin, '%Y-%m-%d %H:%M'))[0] == '-':
        #     messages.error(request,'Result Opening time can not be greater than the Last Login time')
        #     return redirect('./')
      
        ques.des1= request.POST["des1"]
        
        try:
            ques.photo1 = request.FILES["photo1"]
        except:
            ct =1
        try:
            ques.rmin1=request.POST["rmin1"]
            ques.rmin2=int(request.POST["rmin2"])
            ques.rmin3=request.POST["rmin3"]
            ques.rmax1=request.POST["rmax1"]
            ques.rmax2=request.POST["rmax2"]
            ques.rmax3=request.POST["rmax3"]
            ques.mark1=request.POST["mark1"] 
        except ValueError:
            ques.rmin1=0
            ques.rmin2=0
            ques.rmin3=0
            ques.rmax1=0
            ques.rmax2=0
            ques.rmax3=0
            ques.mark1=0


        ques.ques1=request.POST["ques1"]
        ques.ans1=request.POST["ans1"]
        ques.exp1=request.POST["exp1"]
        # ques.mark2=request.POST["mark2"] 
        # ques.ques2=request.POST["ques2"]
        # ques.ans2=request.POST["ans2"]
        # ques.exp2=request.POST["exp2"]       
        # ques.mark3=request.POST["mark3"] 
        # ques.ques3=request.POST["ques3"]
        # ques.ans3=request.POST["ans3"]
        # ques.exp3=request.POST["exp3"]       
        try:
            ques.rmax2 = int(ques.rmax2)
        except ValueError:
            ques.rmax2 = 0 
        # ques.mark4=request.POST["mark4"] 
        # ques.ques4=request.POST["ques4"]
        # ques.ans4=request.POST["ans4"]
        # ques.exp4=request.POST["exp4"]       

        # ques.mark5=request.POST["mark5"] 
        # ques.ques5=request.POST["ques5"]
        # ques.ans5=request.POST["ans5"]
        # ques.exp5=request.POST["exp5"]       
        ques.link=code       
        ques.save()
        messages.success(request,"Question updated")
        return redirect('../')
    return render(request,'CreateAssignment/new.html',{"quest":ques})


def register(request):
    if request.method == 'POST' :
        register = User()
        # if request.POST["college"] == '' or request.POST["roll_no"] == '' or  request.POST["username"]=="" or request.POST["password1"] == ""  or request.POST["password2"]=="":
        #     messages.error(request,'Please fill all the informations!')
        #     return redirect('register')
        # if User.objects.filter(email=request.POST["email"].lower()).first() is not None:
        #     messages.error(request,'A user with that email already exist!')
        #     return redirect('register')
        # if User.objects.filter(username=request.POST["username"].lower()).first() is not None:
        #     messages.error(request,'That username already exist!')
        #     return redirect('register')
        # if request.POST["password1"] != request.POST["password2"] and len(request.Post["password1"]) < 8 :
        #     messages.error(request,'Either the passwords you have entered are not same or the length of passwords is less than 8!')
        #     return redirect('register')
        register.username = request.POST["username"].lower()
        register.email = request.POST["email"].lower()
        register.set_password(request.POST["password1"])
        register.save()
        y = User.objects.filter(username = request.POST["username"].lower()).first().id
        pro = Profile.objects.filter(user_id = y).first()
        pro.college = request.POST["college"]
        pro.roll_no = request.POST["roll_no"]
        if request.POST["role"] == "s": 
            pro.type = 's'
        elif request.POST["role"] == "t":
            pro.type = "t"
        else:
            messages.error(request,"Select the correct role...")
            return redirect('./')
        # pro.avatar = '1'
        pro.save()
        messages.success(request,"Logged In successfully as "+request.POST["username"].lower())
        user = authenticate(request, username = request.POST["username"].lower(), password = request.POST["password1"])
        login(request,user)
        return redirect('email-verify')
    else:
        form =UserRegisterForm()
    return render(request,'users/register.html')


def do_login(request):
    if request.method == 'POST':
        username = request.POST['email'].lower()
        password = request.POST['password']
        print(password)
        try:
            users = User.objects.filter(email=username).first().username
        except:
            users = username
        user = authenticate(request, username=users, password=password)
        if user is not None:
            login(request,user)
            try:
                if request.POST["next"]:
                     return redirect('./../../..'+request.POST["next"])
            except:
                return redirect('CreateAssignment-home')
        else:
            messages.error(request,'Email or Password you have entered is wrong.')
    return render(request,'users/login.html')


def deletequestion(request,link,nu):
    if request.method == 'POST':
        questiondata.objects.filter(id = nu).first().delete()
        return redirect('../')
    return render(request,'CreateAssignment/delete.html')

def student_view(request,link):
    code= createlink.objects.filter(link = link).first()
   
    print(custom)
    if request.user.profile.type == "t":
        return redirect("../")
    mydata = st_data()
    if request.method == 'POST':
        mydata.answer = request.POST["answer"]
        mydata.username_id = int(request.user.id)
        mydata.link_id = code.id
        mydata.save()
        return redirect('CreateAssignment-home')    
    return render(request,'CreateAssignment/summary.html',{"cus":custom})
    

        
       