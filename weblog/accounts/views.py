from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None :
                login(request, user)
                messages.success(request, 'Login is Success','success')
                return redirect('blog:home')
            else :
                messages.error(request, 'wrong username or password','danger')
    else :
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def user_register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #cd = cleaned data
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'you registered successfully', 'success')
            return redirect('accounts:login')

    else :
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)



