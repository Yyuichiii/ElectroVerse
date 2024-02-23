from django.shortcuts import render,redirect
from .models import Component,Product




def Components_view(request,Category,type):
    try:
        
        component=Component.objects.get(Type=type)  
        return render(request,'Components/Components_content.html',{'component':component})
    
    except:
        
        return redirect('home')

def Products_list_view(request, *args, **kwargs):
        type_value = request.GET.get('type')
        products=Product.objects.filter(Type=type_value)

        # component=Component.objects.get(Type=type_value)
        return render(request,'Components/products_list.html',{'Products':products})
    # except:
    #     print('sdf')
    #     return render(request,'Components/products_list.html')

from django.shortcuts import get_object_or_404
def Products_Content_view(request,pk):
     print(pk)
     product = get_object_or_404(Product, pk=pk)
     return render(request,'Components/products_content.html',{'Product':product})
     