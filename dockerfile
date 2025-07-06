FROM python:3.11.1

WORKDIR /app

# Install system dependencies and Microsoft ODBC Driver 18 for SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    gcc \
    g++ \
    unixodbc \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . /app

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001"]