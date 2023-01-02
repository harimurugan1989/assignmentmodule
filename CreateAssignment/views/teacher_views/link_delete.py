from django.contrib import messages
from CreateAssignment.models import CreateLink
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def LinkDelete(request,link):
    if request.method == "POST":
       x = CreateLink.objects.filter(link = link).all().delete()
       messages.success(request,"Assignment has been deleted successfully")
       return redirect('/')
    return render(request,"CreateAssignment/deletelink.html")
