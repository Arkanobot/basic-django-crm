from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    
    
    #check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("home")
    else:    
        return render(request, "home.html", {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out, Have a great day!")
    return render(request, "home.html",{})

def register_user(request): 
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #login after register
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form':form})
        
    return render(request, "register.html", {'form':form})



def customer_record(request, pk):
    #check if user is logged in
    if request.user.is_authenticated:
        #look up the record
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {'customer_record': customer_record})
    else:
        messages.error(request, "You must be logged in to view that page")
        return redirect("home")