# Dockerfile

FROM python:3.11-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de dependência
COPY requirements.txt requirements-dev.txt ./

# Instalar pacotes Python
RUN pip install --upgrade pip && pip install -r requirements-dev.txt

# Copiar o restante da aplicação
COPY . .

# Comando padrão (você pode ajustar para outro entrypoint)
CMD ["flask", "--app", "src.main:create_flask_app", "run", "--host=0.0.0.0", "--port=5000"]

