from asyncio.windows_events import NULL
import datetime 
from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Question, createlink, Instruction, Profile, Student
from django.shortcuts import redirect, render
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DeleteView
from django.contrib import messages

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

def randnumber(a,b):
    return random.randint(a,b)

# Create your views here.
@login_required
def linkcreate(request):
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

            create = createlink()
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
                if createlink.objects.filter(link= link).first() is None:
                    break
            create.link= link
            create.save()
            Instruction.objects.create(instructions= "", assignment_id = create.id )
            messages.success(request,f"Assignment has been created successfully!")
            return redirect("../"+link+"/")
        return render(request,"CreateAssignment/home.html")
    elif pro.type =='s':
        return render(request,'CreateAssignment/something.html',{'msg':"Student profile is not permitted to create Assignment"})


@login_required
def summary(request,link):
    pro=Profile.objects.filter(user=request.user).first()
    if pro.type=='t':
        codes_id=createlink.objects.filter(link=link).first()
        content=[]
        dic={}
        ques = Question.objects.filter(assignment_id=codes_id.id).all()
        num= 1
        for questiondatas in ques:
            questions={}
            questions["question"]=questiondatas.question
            questions["explanation"]=questiondatas.explanation
            questions["ques_num"]=num
            content.append(questions)
            num+=1
        dic={"questions":reversed(content)}
        return render(request, "CreateAssignment/summary.html", {"assign": codes_id,"content":dic})
    elif pro.type=='s':
        code = createlink.objects.filter(link=link).first()
        inst = Instruction.objects.filter(assignment_id = code.id).first()
        instructions = inst.instructions.split('\n')
        num_of_ques = Question.objects.filter(assignment_id=code.id).count()
        nos=Student.objects.filter(username=request.user,link_id=code.id).count()
        ques_all=Question.objects.filter(assignment_id=code.id).all()
        data_m=Student.objects.filter(username=request.user,link_id=code.id,qno=nos+1).first()
        j=0
        while(nos<num_of_ques):
            ques=ques_all[j]
            if data_m is None:
                data=Student()       
                rand_arr=[]
                data.username=request.user
                data.link_id = code.id
                data.qno_id=ques.id
                r=1
                i='$'+str(r)
                while(ques.question.find(i)!=-1):
                    x=randnumber(int(ques.rand_variable_min),int(ques.rand_variable_max))
                    rand_arr.append(x)
                    r+=1
                    i='$'+str(r)
                data.R=rand_arr
                data.save()
                nos+=1
                j+=1
        return render(request,"CreateAssignment/stu_instructions.html",{"lines" : instructions,"assign": code,"noq":num_of_ques })

@login_required
def instructions(request,link):
    code = createlink.objects.filter(link=link).first()
    inst = Instruction.objects.filter(assignment_id = code.id).first()
    if request.method == "POST":
        inst.instructions = request.POST["instructions"]
        inst.save()
        messages.success(request,f"Instructions have been updated successfully!")
        return redirect("./")
    return render(request,"CreateAssignment/instructions.html",{"instruction" : inst})

@login_required
def edit(request,link):
    codes = createlink.objects.filter(link = link).all()
    if request.method == 'POST':
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

        for code in codes:
            code.course_name = request.POST["course_name"].strip().replace(" ","-")
            code.assignment_name = request.POST["assignment_name"].strip().replace(" ","-")
            code.start = request.POST["start"]
            code.first_sub_time = request.POST["first_sub_time"]
            code.extend = request.POST.get("extend",False)
            code.second_sub_time = request.POST["second_sub_time"]
            code.no_of_submissions = request.POST["no_of_submissions"] 
            code.perc_penalty = request.POST["perc_penalty"]
            code.notif = request.POST["notif"] 
            code.face_rec = request.POST["face_rec"]
            code.neg_mark = request.POST["neg_mark"] 
            code.res_anno= request.POST["res_anno"]
            code.creator_id = request.user.id
            code.result_time = request.POST["result_time"]
            code.save()
        messages.success(request,"Settings Updated Successfully")
        return redirect('./')
    code = codes.first()
    start_v=str(code.start)[:10]+'T'+str(code.start)[11:16]
    first_sub_time_v=str(code.first_sub_time)[:10]+'T'+str(code.first_sub_time)[11:16]
    second_sub_time_v=str(code.second_sub_time)[:10]+'T'+str(code.second_sub_time)[11:16]
    result_time_v=str(code.result_time)[:10]+'T'+str(code.result_time)[11:16]
    data = {"course_name":code.course_name,"assignment_name":code.assignment_name,"start":start_v,"first_sub_time":first_sub_time_v,"extend":code.extend,"second_sub_time":second_sub_time_v,"code_id":code.id,"no_of_submissions":code.no_of_submissions,"perc_penalty":code.perc_penalty,"notif":code.notif,"face_rec":code.face_rec, "neg_mark":code.neg_mark,"res_anno": code.res_anno,"result_time":result_time_v}
    return render(request,'CreateAssignment/settings.html',data)

@login_required
def linkdelete(request,link):
    if request.method == "POST":
       x = createlink.objects.filter(link = link).all().delete()
       messages.success(request,"Assignment has been deleted successfully")
       return redirect('/')
    return render(request,"CreateAssignment/deletelink.html")

@login_required
def questions(request,link):
    pro=Profile.objects.filter(user=request.user).first()
    ques = Question()
    if request.method == "POST":
        ques.assignment_id = createlink.objects.filter(link =link).first().id
        ques.question = request.POST["question"]
        ques.rand_variable_min=request.POST["rand_variable_min"]
        ques.rand_variable_max=request.POST["rand_variable_max"]
        ques.explanation = request.POST["explanation"]
        ques.save()
        messages.success(request,f"Question has been added successfully!")
        return redirect("../")
    return render(request,"CreateAssignment/questions.html")
   
   
@login_required
def edit_question(request,link,qno):
    codes_id=createlink.objects.filter(link=link).first()
    ques = Question.objects.filter(assignment_id=codes_id.id).all()
    id_first=ques.values_list('id',flat=True).first()
    change = Question.objects.filter(id=id_first+qno-1).first()
    if request.method == "POST":
        change.question = request.POST["question"]
        change.rand_variable_min=request.POST["rand_variable_min"]
        change.rand_variable_max=request.POST["rand_variable_max"]
        change.explanation = request.POST["explanation"]
        change.save()
        messages.success(request,f"Question has been updated successfully!")
        return redirect("../../")    
    return render(request,"CreateAssignment/edit_question.html",{"questions":change})

@login_required
def delete_question(request,link,qno):
    if request.method =='POST':
        codes_id=createlink.objects.filter(link=link).first()
        ques = Question.objects.filter(assignment_id=codes_id.id).all()
        id_first=ques.values_list('id',flat=True).first()
        Question.objects.filter(id = id_first+qno-1).first().delete()
        messages.success(request,f"Question has been deleted successfully!")
        return redirect('../../')
    return render(request,"CreateAssignment/delete_question.html")

def register(request):
    if request.method == 'POST' :
        register = User()
        if request.POST["college"] == '' or request.POST["roll_no"] == '' or  request.POST["username"]=="" or request.POST["password1"] == ""  or request.POST["password2"]=="":
            messages.error(request,'Please fill all the information!')
            return redirect('./')
        register.username = request.POST["username"].lower()
        register.email = request.POST["email"].lower()
        if request.POST["password1"]==request.POST["password2"]:
            register.set_password(request.POST["password1"])
            register.save()
            pro=Profile()
            y = User.objects.filter(username = request.POST["username"].lower()).first()
            pro.user_id=y.id
            pro.roll_no = request.POST["roll_no"]
            pro.college = request.POST["college"]
            pro.type = request.POST["role"]
            pro.save()
            messages.success(request,"Registered successfully as "+request.POST["username"].lower())
            return redirect('./')
        else:
            messages.error(request,"Passwords did not match")
            return redirect('./')
    return render(request,'CreateAssignment/register.html')
        
def do_login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            pro=Profile.objects.filter(user=user).first()
            login(request,user)
            messages.success(request,"Logged in successfully as "+request.POST["username"].lower())
            if pro.type =='t':
               return redirect('/')
            elif pro.type=='s':
                return redirect('./')
        else:
            messages.error(request,'Username or Password you have entered is wrong.')
            return redirect('./')
    return render(request,'CreateAssignment/login.html')

def do_logout(request):
    logout(request)
    return render(request,'CreateAssignment/logout.html')

@login_required
def take_assignment(request,link):
    codes_id=createlink.objects.filter(link=link).first()
    all_sections=[]
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
    
