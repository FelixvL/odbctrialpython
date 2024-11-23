# Gebruik een basis Python image
FROM python:3.9-slim

# Installeer vereiste pakketten en ODBC-drivers
RUN apt-get update && apt-get install -y \
    curl apt-transport-https gnupg unixodbc unixodbc-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    pip install pyodbc

# Kopieer het Python-script naar de container
COPY trial.py /app/trial.py

# Zet de werkdirectory
WORKDIR /app

# Voer het script uit
CMD ["python", "trial.py"]
