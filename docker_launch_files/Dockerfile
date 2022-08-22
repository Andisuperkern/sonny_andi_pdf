FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y &&\
    apt-get install -y --no-install-recommends &&\
    apt-get install python3.8 -y &&\
    apt install python3-pip -y &&\
    pip install --upgrade pip

RUN pip install Django==3.1.5 &&\
    pip install pytz==2017.2 &&\
    pip install django-crispy-forms

    # pip install django-filter==21.1 &&\
    # pip install Pillow==5.2.0 &&\
    # pip install djangorestframework==3.13.1 &&\
    # pip install django-rest-auth==0.9.5


#CMD ["python3", "manage.py runserver 0.0.0.0:8000"]
CMD ["bin/bash"]