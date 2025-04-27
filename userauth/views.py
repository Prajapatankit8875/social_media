from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . models import Profile

# Create your views here.
def signup(request):
    try:
        if request.method=='POST':
            fname = request.POST.get('fname')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')
            my_user = User.objects.create_user(fname, emailid, pwd)
            my_user.save()
            user_model = User.objects.get(username=fname)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request,my_user)
                return redirect('/') 
            return redirect('/login')
    except:
        invalid="User Already Exists"
        return render(request, 'signup.html', {'invalid': invalid}) 
    return render(request, 'signup.html') 

def login(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/')
        invalid="Invalid Credentials"
        return render(request, 'login.html', {'invalid': invalid}) 
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('/login')

def home(request):
    return HttpResponse("Hello, world. You're at the userauth home page.")