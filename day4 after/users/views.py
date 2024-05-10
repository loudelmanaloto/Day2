from django.shortcuts import render, redirect

# Create your views here.

#import libraries for login, logout, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "There is an error when logging in.")
            return redirect('login')

    return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect('login')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered successfully.")
            return redirect('index')
        else:
            messages.error(request, "There is a problem registering.")
            return redirect('register')
    return render(request, 'authenticate/register.html', {"form":form})
