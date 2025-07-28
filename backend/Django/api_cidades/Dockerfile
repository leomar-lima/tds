# 1. Imagem base com Python
FROM python:3.11.6-slim-bullseye

# 2. Define o diretório de trabalho
WORKDIR /home/app

# 3. Copia apenas o requirements.txt e instala dependências
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 4. Copia o restante do projeto
COPY . .

# 5. Expõe a porta da aplicação
EXPOSE 8000

# 6. Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
