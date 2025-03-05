# Usa una imagen base de Python
FROM python:3.10

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
