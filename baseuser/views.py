from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .forms import RegisterForm, LoginForm
from django import forms


def register(request):
    form = RegisterForm()
    if request.method =='POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save
            
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'user_form' : form,
    }            
    return render(request, 'register.html', context)

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(usename=username, password=password)
            if user is not None:
                django_login(request,user)
                return redirect('home')
            else:
                raise forms.ValidationError('User not found')

        else:
            form = LoginForm()
    context = {
        'login_form' : form,
    }      
    return render(request, 'login.html', context)

@login_required
def logout(request):
    django_logout(request)
    return redirect ('home')
