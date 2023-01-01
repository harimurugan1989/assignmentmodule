from CreateAssignment.models import CreateLink, Profile
from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required


def randnumber(a,b):
    return random.randint(a,b)

@login_required
def asummary(request):
    pro=Profile.objects.filter(user=request.user).first()
    if pro.type=='t':
        codes=CreateLink.objects.filter(creator=request.user).all()
        return render(request, "CreateAssignment/safebook.html", {"simple": codes})
