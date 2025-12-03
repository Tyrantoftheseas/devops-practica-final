# Usar una imagen base ligera de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los requerimientos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la app
COPY . .

# Exponer el puerto 5000
EXPOSE 5000

# Comando para correr la app
CMD ["python", "app.py"]