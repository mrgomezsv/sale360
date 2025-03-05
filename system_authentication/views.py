from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home_view(request):
    return redirect('login')  # Redirige a la vista de login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio después del login
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')  # Renderiza la plantilla en system_authentication/templates/login.html