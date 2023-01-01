from django.contrib import messages
from CreateAssignment.models import CreateLink, Instruction
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def Instructions(request,link):
    code = CreateLink.objects.filter(link=link).first()
    inst = Instruction.objects.filter(assignment_id = code.id).first()
    if request.method == "POST":
        inst.instructions = request.POST["instructions"]
        inst.save()
        messages.success(request,f"Instructions have been updated successfully!")
        return redirect("./")
    return render(request,"CreateAssignment/instructions.html",{"instruction" : inst})

