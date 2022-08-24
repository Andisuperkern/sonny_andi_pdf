FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y &&\
    apt-get install -y --no-install-recommends &&\
    apt-get install python3.8 -y &&\
    apt install python3-pip -y &&\
    pip install --upgrade pip

RUN pip install Django==3.1.5 \
                pytz==2017.2 \
                django-crispy-forms \
                pytest==7.1.2
                
WORKDIR /sonny_andi_pdf
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
