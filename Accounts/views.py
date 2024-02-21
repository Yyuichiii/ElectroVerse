from django.shortcuts import render,redirect
from .forms import LoginForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse,HttpResponse
from .models import Cart
from Components.models import Product
from django.db.models import Sum
# Create your views here.

def home(request):
    return render(request,"Accounts/home.html")

def registration(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account has been Successfully Created !!!")
            return redirect('login')
        return render(request,"Accounts/Register.html",{'form': form})

    else:
        form=UserCreationForm()
        return render(request,"Accounts/Register.html",{'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            uemail=form.cleaned_data['email'] 
            upas=form.cleaned_data['password']
            user = authenticate(email=uemail,password=upas)
            if user is not None:
                login(request,user)
                messages.success(request, "Login Successfully !!!")                
                return redirect('home')
            
    
    return render(request,"Accounts/Login.html",{'form': form})
    

def logout_view(request):
    logout(request)
    messages.success(request, "Logout Successful !!!")
    return redirect('login')


# Django View for handling Ajax request
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "Login Required")
        return render(request,"Accounts/partial/cart_not_login.html")

    product=Product.objects.get(pk=product_id)

    if not Cart.objects.filter(user=request.user ,Pid=product).exists():
        cart=Cart.objects.create(user=request.user,Pid=product)
        cart.save()

    else:
        cart=Cart.objects.get(user=request.user,Pid=product)
        cart.Quantity=cart.Quantity+1
        cart.save()
    cartt = Cart.objects.filter(user=request.user).aggregate(total_quantity=Sum('Quantity'))
    messages.success(request, "%s has been added to the cart" % product)
    return render(request,"Accounts/partial/cart_update.html",{'cart':cartt['total_quantity'],'product':product_id})

