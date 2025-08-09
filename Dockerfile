FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpoppler-cpp-dev poppler-utils git && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
