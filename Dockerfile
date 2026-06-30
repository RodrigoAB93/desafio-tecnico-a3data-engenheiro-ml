FROM python:3.11-slim

WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia a aplicação
COPY app/ ./app/

# Copia os testes
COPY tests/ ./tests/

# (Opcional) Copia o README
COPY readme.md .

# Expõe a porta da API
EXPOSE 8000

# Inicia a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]