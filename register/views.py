from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib import messages

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'Your registration was successful. Thank you for joining us. ')
            
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
