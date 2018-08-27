FROM python:3.6

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV PYTHONPATH $PYTHONPATH:.

RUN apt-get update && apt-get -y upgrade && apt-get -y install kmod
