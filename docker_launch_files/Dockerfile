FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y &&\
    apt-get install -y --no-install-recommends &&\
    apt-get install python3.8 -y &&\
    apt install python3-pip -y &&\
    pip install --upgrade pip

RUN pip install Django==3.1.5 &&\
    pip install pytz==2017.2 &&\
    pip install django-crispy-forms &&\
    pip install djangorestframework

CMD ["python3", "/sonny_andi_pdf/manage.py", "runserver", "0.0.0.0:8000"]