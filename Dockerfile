FROM python:3.10-buster

RUN adduser --system --no-create-home dj

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

RUN python manage.py collectstatic --no-input --clear -v 0

USER dj