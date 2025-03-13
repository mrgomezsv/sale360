from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Usar PostgreSQL
        'NAME': os.getenv('POSTGRES_DB'),          # Nombre de la base de datos
        'USER': os.getenv('POSTGRES_USER'),        # Usuario de la base de datos
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),# Contraseña del usuario
        'HOST': os.getenv('POSTGRES_HOST'),        # Dirección IP del servidor
        'PORT': os.getenv('POSTGRES_PORT'),        # Puerto de PostgreSQL
        'OPTIONS': {
            'sslmode': 'require',  # Usar SSL
        },
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_&5ma67!huyah$)hh=2rv9c-e=$5q&+7b^hg4!68es8@@sx!$)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Permitir todos los hosts en desarrollo (cambia esto en producción)
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'system_accounting',
    'system_authentication',
    'system_dashboard',
    'system_dte_sv',
    'system_employees',
    'system_inventory',
    'system_invoicing',
    'system_payroll',
    'system_sales',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Añade esto
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'Sale360.urls'

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Carpeta donde se recopilarán los archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Carpeta donde tienes tus archivos estáticos en desarrollo
]

# Configuración de archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración WSGI
WSGI_APPLICATION = 'Sale360.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Asegúrate de que esta línea esté presente
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGIN_REDIRECT_URL = 'dashboard'  # Redirige al dashboard después del login
LOGOUT_REDIRECT_URL = 'login'  # Redirige al login después del logout
