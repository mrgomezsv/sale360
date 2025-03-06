from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class RegisterForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=150, required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(label="Primer Nombre", max_length=30, required=True)
    second_name = forms.CharField(label="Segundo Nombre", max_length=30, required=False)
    third_name = forms.CharField(label="Tercer Nombre", max_length=30, required=False)
    first_lastname = forms.CharField(label="Primer Apellido", max_length=30, required=True)
    second_lastname = forms.CharField(label="Segundo Apellido", max_length=30, required=False)
    third_lastname = forms.CharField(label="Tercer Apellido", max_length=30, required=False)
    age = forms.IntegerField(label="Edad", required=True)
    email = forms.EmailField(label="Correo Electrónico", required=True)
    position = forms.CharField(label="Cargo", max_length=100, required=True)
    company = forms.CharField(label="Empresa", max_length=100, required=True)
    is_root = forms.BooleanField(label="Root", required=False)
    phone = forms.CharField(label="Teléfono", max_length=15, required=True)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{6,}$', password):
            raise ValidationError("La contraseña debe tener al menos 6 caracteres, una letra, un número y un símbolo.")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?\d{9,15}$', phone):
            raise ValidationError("El número de teléfono no es válido.")
        return phone
