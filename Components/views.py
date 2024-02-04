from django.shortcuts import render,redirect
from .models import Passive,Active

# Create your views here.
def passive(request,type):
    try:
        component=Passive.objects.get(type=type)
    
        return render(request,'Components/Passive.html',{'component':component})
    
    except:
        return redirect('home')
    

def active(request,type):
    try:
        component=Active.objects.get(type=type)
    
        return render(request,'Components/Active.html',{'component':component})
    
    except:
        return redirect('home')