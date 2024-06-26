from django.shortcuts import render,redirect
from .models import Component,Product
from django.shortcuts import get_object_or_404




def Components_view(request,Category,type):
    try:
        
        component=Component.objects.get(Type=type)  
        return render(request,'Components/Components_content.html',{'component':component})
    
    except:
        
        return redirect('home')

def Products_list_view(request, *args, **kwargs):
        type_value = request.GET.get('type')
        products=Product.objects.filter(Type=type_value)
        return render(request,'Components/products_list.html',{'Products':products})



def Products_Content_view(request,pk):    
    product = get_object_or_404(Product, pk=pk)
    return render(request,'Components/products_content.html',{'Product':product})
     