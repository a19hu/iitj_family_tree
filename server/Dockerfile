FROM python:3.11-slim

WORKDIR /myapp

COPY requirements.txt ./

# Install PostgreSQL client for the wait script
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN bash ./Script.sh

COPY . .

# Make wait-for-db.sh executable
RUN chmod +x wait-for-db.sh

EXPOSE 8000

# Wait for database then start server
CMD ["./wait-for-db.sh", "db", "python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]



