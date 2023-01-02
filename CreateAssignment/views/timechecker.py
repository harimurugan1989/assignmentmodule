from CreateAssignment.models import CreateLink, Instruction
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .duration import Duration

@login_required
def TimeChecker(request,link):
    link_data= CreateLink.objects.filter(link =link).first()
    if link_data is None:
        return render(request,"public/something.html",{'msg':"Check your link again. This Link is not valid.","videos":topThree()})
    if request.user.profile.type == "t":
        return redirect("./")
    start_d = str(link_data.start).split('+')[0]
    first_d=str(link_data.first_sub_time).split('+')[0]
    oc=Duration(start_d,first_d)
    insts = []
    insta = Instruction.objects.filter(assignment_id = link_data.id).first()
    if insta != None:
        inst = insta.instructions
        for each in inst.split("\n"):
            if len(each.strip()) < 1:
                continue
            insts.append(each)
    if oc == 1:
        # needs to be completed for assignment page
            # return redirect('./test')
        return render(request,'CreateAssignment/stu_instructions.html',{"link":link,"given":["yze-bdxr-hmo","hyr-amzo-igc","tqz-nhvm-vid"],"endtime":first_d,"inst":insts,"assign":link_data})
    elif oc == 2:
        return render(request,'CreateAssignment/stu_instructions.html',{'msg':'Assignment has not started yet',"link":link,"time":start_d,"inst":insts,"assign":link_data})
    elif oc == 3:
        return render(request,'CreateAssignment/something.html',{'msg':'Assignment deadline is reached, better luck next time'})
    else:
        return render(request,'CreateAssignment/something.html',{'msg':'Getting some error while loading please try later'})



