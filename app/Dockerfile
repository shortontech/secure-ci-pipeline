FROM python:3.11-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get upgrade -y && pip install --upgrade pip && pip install -r requirements.txt
COPY src/ .
EXPOSE 8000
CMD ["python", "main.py"]