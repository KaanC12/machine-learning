# The project runs in python 3.11
FROM python:3.11-slim

# Working repository
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements
COPY requirements.txt .

# Run installition
RUN pip install --no-cache-dir -r requirements.txt

# Copies from to 
COPY src ./src
COPY database ./database

# Run commands
CMD [ "python", "src/app.py"]