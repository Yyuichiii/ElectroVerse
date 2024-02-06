from django.shortcuts import render,redirect
from .models import Component


def Components_view(request,Category,type):
    try:
        component=Component.objects.get(Type=type)  
        return render(request,'Components/Components_content.html',{'component':component})
    
    except:
        return redirect('home')
