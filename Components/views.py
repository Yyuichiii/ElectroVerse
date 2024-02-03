from django.shortcuts import render,redirect
from .models import Passive

# Create your views here.
def passive(request,type):
    try:
        component=Passive.objects.get(type=type)
    
        return render(request,'Components/Passive.html',{'component':component})
    
    except:
        return redirect('home')