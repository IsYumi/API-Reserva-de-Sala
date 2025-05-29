# Imagem base
FROM python:3.10-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY . .

# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta da aplicação Flask
EXPOSE 5001

# Comando para rodar a aplicação
CMD ["python", "app.py"]
