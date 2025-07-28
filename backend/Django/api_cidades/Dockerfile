FROM python:3.10-slim

# 1. Defina diretório de trabalho
WORKDIR /home/app

# 2. Copie o requirements.txt
COPY requirements.txt .

# 3. Instale as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# 4. Copie todo o código
COPY . .

# 5. Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
