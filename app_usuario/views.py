from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages

def login_usuario(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login') 

