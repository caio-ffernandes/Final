FROM python:3.9

# Define o diretório de trabalho no contêiner como a raiz do projeto
WORKDIR /app

# Copia todos os arquivos da pasta Back (que será a raiz agora) para /app
COPY ./ /app/

# Copia o arquivo de dependências
COPY ./requirements.txt /app/requirements.txt

# Instala as dependências
RUN pip install -r /app/requirements.txt

# Define o PYTHONPATH, já que o código estará diretamente em /app
ENV PYTHONPATH=/app

# Comando para iniciar o servidor, apontando diretamente para o main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
