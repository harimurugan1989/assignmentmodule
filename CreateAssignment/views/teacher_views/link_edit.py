import datetime 
from django.contrib import messages
from CreateAssignment.models import CreateLink
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def LinkEdit(request,link):
    codes = CreateLink.objects.filter(link = link).all()
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

