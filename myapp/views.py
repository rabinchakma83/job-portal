

from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate, login
from .models import User, RecruiterProfile, JobSeekerProfile

# Create your views here.
def home (request):
    

    return render(request, 'index.html')
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)   
        if form.is_valid():
            password = form.cleaned_data.get('password1') 
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()               
    return render(request, 'register.html', {'form': form})
def Login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

    
