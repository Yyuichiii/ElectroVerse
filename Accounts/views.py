from django.shortcuts import render,redirect
from .forms import LoginForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse,HttpResponse
from .models import Cart
from Components.models import Product
from django.db.models import Sum,F

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

from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):
    products=Cart.objects.filter(user=request.user)
    tp = products.aggregate(total_price=Sum(F('Pid__Price') * F('Quantity')))
    return render(request,"Accounts/cart.html",{'products': products,'Price':tp['total_price']})


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

def qupdt(request, id,c):
    
    # Fetch the cart object by its primary key
    cart=Cart.objects.get(pk=id)

    if c=='add':
        # Increment the quantity
        cart.Quantity=cart.Quantity+1
        cart.save()
        # Display success message
        messages.success(request, f"Quantity of {cart.Pid} has been increased")
    else:
        if cart.Quantity==1:
            # Display success message
            messages.error(request, f"Quantity of {cart.Pid} cannot be less than 1")
        else:
            # Decrement the quantity
            cart.Quantity=cart.Quantity-1
            cart.save()
            # Display success message
            messages.success(request, f"Quantity of {cart.Pid} has been decreased")


    # Fetch all products in the cart for the user
    products=Cart.objects.filter(user=request.user)

    # Aggregate total quantity and total price
    totals = products.aggregate(total_quantity=Sum('Quantity'), total_price=Sum(F('Pid__Price') * F('Quantity')))


    # Render the template with necessary data
    return render(request,"Accounts/partial/quantity_update.html",{
        'cart':totals['total_quantity'],
        'product':cart,
        'Price':totals['total_price']        
    })


def remove_cart(request,id):
    #Fetch the cart object by its primary key
    cart=Cart.objects.get(pk=id)

    #delete the cart object
    cart.delete()
    
    # Display success message
    messages.success(request, f"The product has been removed from the cart")
    return redirect('Cart')
    


