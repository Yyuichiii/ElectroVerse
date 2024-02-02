from django.shortcuts import render,redirect
from .forms import LoginForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


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