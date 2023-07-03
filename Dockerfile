FROM python:3.11.3-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY src/ /app


ENTRYPOINT ["python", "app.py"]
