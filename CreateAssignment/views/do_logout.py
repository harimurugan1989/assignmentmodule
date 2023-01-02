from django.contrib.auth import logout
from django.shortcuts import render

def DoLogout(request):
    logout(request)
    return render(request,'CreateAssignment/logout.html')