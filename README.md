# Sale360 - Sistema de Punto de Ventas
Sale360 es un sistema de punto de ventas desarrollado en Django que incluye funcionalidades como gestión de inventario, facturación, nóminas de empleados, devoluciones, tickets de ventas, y más. Este proyecto utiliza SQLite como base de datos inicial y está diseñado para ser escalable y fácil de mantener.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

Python 3.8 o superior.
Visual Studio Code (VSCode) o cualquier editor de texto de tu preferencia.
Git (opcional, para control de versiones).
Instalación y configuración

Sigue estos pasos para configurar el proyecto en tu entorno local.

### 1. Clonar el repositorio (opcional)

Si estás usando Git, clona el repositorio:

bash
Copy
git clone https://github.com/tu-usuario/Sale360.git
cd Sale360
### 2. Crear un entorno virtual

Crea un entorno virtual para aislar las dependencias del proyecto:

bash
Copy
python -m venv venv
### 3. Activar el entorno virtual

Windows:
bash
Copy
.\venv\Scripts\activate
macOS/Linux:
bash
Copy
source venv/bin/activate
### 4. Instalar dependencias

Instala Django y otras dependencias necesarias:

bash
Copy
pip install django
### 5. Crear el proyecto Django

Crea el proyecto Django con el nombre Sale360:

bash
Copy
django-admin startproject Sale360 .
### 6. Configurar la base de datos (SQLite)

Django ya está configurado para usar SQLite por defecto. No es necesario realizar cambios en settings.py.

### 7. Aplicar migraciones iniciales

Ejecuta las migraciones para crear las tablas necesarias en la base de datos:

bash
Copy
python manage.py migrate
### 8. Crear un superusuario

Crea un superusuario para acceder al panel de administración de Django:

bash
Copy
python manage.py createsuperuser
### 9. Ejecutar el servidor de desarrollo

Inicia el servidor de desarrollo para ver el proyecto en acción:

bash
Copy
python manage.py runserver
Visita http://127.0.0.1:8000/ en tu navegador para ver la página de bienvenida de Django.

Estructura del proyecto

El proyecto tiene la siguiente estructura inicial:

Copy
Sale360/
├── manage.py
├── Sale360/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
Comandos útiles

Crear una nueva aplicación:
bash
Copy
python manage.py startapp nombre_app
Aplicar migraciones después de cambios en los modelos:
bash
Copy
python manage.py makemigrations
python manage.py migrate
Acceder al panel de administración:
Visita http://127.0.0.1:8000/admin/ e inicia sesión con el superusuario.
Desactivar el entorno virtual:
bash
Copy
deactivate
Despliegue

Para desplegar el proyecto en un entorno de producción, considera usar:

Base de datos: PostgreSQL o MySQL.
Servidor web: Gunicorn + Nginx.
Plataforma de despliegue: Heroku, AWS, o DigitalOcean.
Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama con tu nueva funcionalidad (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').
Sube los cambios a tu repositorio (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Nombre: Mario Roberto
Email: mrgomez.dev@gmail.com
GitHub: tu-usuario
¡Gracias por usar Sale360! 🚀

### Aplicar migraciones con el docker corriendo

mrgomez@MacBook-Pro-de-Mario Sale360 % docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
