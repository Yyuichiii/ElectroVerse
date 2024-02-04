from django.shortcuts import render,redirect
from .models import Passive,Active,Electromechanical,Display,Sensor

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
    

def electromechanical(request,type):
    try:
        component=Electromechanical.objects.get(type=type)   
        return render(request,'Components/Electromechanical.html',{'component':component})
    
    except:
        return redirect('home')
    
def display(request,type):
    try:
        component=Display.objects.get(type=type)   
        return render(request,'Components/Electromechanical.html',{'component':component})
    
    except:
        return redirect('home')
    
       
def sensor(request,type):
    try:
        component=Sensor.objects.get(type=type)   
        return render(request,'Components/Electromechanical.html',{'component':component})
    
    except:
        return redirect('home')