# Usamos una imagen base ligera de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos solo el archivo de dependencias primero para aprovechar el cache de Docker
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# El puerto que expone la aplicación Flask (coincide con app.py)
EXPOSE 1002

# Comando por defecto para ejecutar la aplicación
CMD ["python", "app.py"]