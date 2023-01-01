from django.contrib import messages
from django.contrib.auth import authenticate,login
from CreateAssignment.models import Profile
from django.shortcuts import redirect, render
from django.contrib import messages

def DoLogin(request):
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