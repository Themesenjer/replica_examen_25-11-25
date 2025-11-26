# Imagen base ligera
FROM python:3.10-slim

# Evitar preguntas y mejorar seguridad
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecemos directorio de trabajo
WORKDIR /app

# Instalamos dependencias de sistema si tu proyecto las necesita
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar solo requirements.txt para cache
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer puerto Flask
EXPOSE 1002

# Comando por defecto
CMD ["python", "app.py"]
