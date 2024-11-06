# Usa una base Python compatibile con MutPy
FROM python:3.12

# Installa le dipendenze per MutPy
RUN pip install --no-cache-dir mutpy

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia il progetto nel container
WORKDIR /app
COPY . .

# Comando di default per eseguire MutPy
ENTRYPOINT ["mut.py"]