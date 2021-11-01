# syntax=docker/dockerfile:1
FROM python:3
RUN pip install pipenv
RUN python -m pip install Django
RUN python -m pip install Celery
RUN python -m pip install requests
RUN python -m pip install redis
RUN python -m pip install django_celery_beat
RUN python -m pip install speedtest-cli
RUN python -m pip install psycopg2
RUN python -m pip install djangorestframework
RUN python -m pip install django-cors-headers
RUN python -m pip install python-dotenv
ENV PYTHONUNBUFFERED=1
WORKDIR /exchage_rate
COPY requirements.txt /exchage_rate/
RUN pip install -r requirements.txt
COPY . /exchage_rate/
#port from the container to expose to host
EXPOSE 8000
#Tell image what to do when it starts as a container
CMD /code/start.sh