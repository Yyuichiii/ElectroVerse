from django.shortcuts import render,redirect
from .models import Component


def Components_view(request,Category,type):
    try:
        
        component=Component.objects.get(Type=type)  
        return render(request,'Components/Components_content.html',{'component':component})
    
    except:
        
        return redirect('home')

def Products_list_view(request, *args, **kwargs):
        type_value = request.GET.get('type')
        print(type_value)
        # component=Component.objects.get(Type=type_value)
        return render(request,'Components/products_list.html')
    # except:
    #     print('sdf')
    #     return render(request,'Components/products_list.html')