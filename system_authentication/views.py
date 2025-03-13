from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm


def home(request):
    return redirect('login')  # Redirige a la página de login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")  # Depuración
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Usuario autenticado correctamente")  # Depuración
            login(request, user)
            print("Redirigiendo al dashboard")  # Depuración
            return redirect('dashboard')
        else:
            print("Usuario o contraseña incorrectos")  # Depuración
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = User.objects.create_user(
                username=form.cleaned_data['username'],  # Nombre de usuario
                email=form.cleaned_data['email'],  # Email
                password=form.cleaned_data['password'],  # Contraseña
                first_name=form.cleaned_data['first_name'],  # Nombre
                last_name=form.cleaned_data['first_lastname'],  # Apellido
            )
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('register')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
