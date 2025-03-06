from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        #check to see if logged in
        username = request.POST['username']
        password = request.POST['password']
        
        #Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in ")
            return redirect('home')
        else:
            messages.success(request,"There is an error , please TRY again...")
        
    return render(request,'home.html',{})

def login_user(request):
    pass

def logout_user(request):
    pass
