#DockerFile 
FROM python:3.11-slim

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory 
WORKDIR /app

#install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

#copy project files 
COPY . .

#run migrations and start server 
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
