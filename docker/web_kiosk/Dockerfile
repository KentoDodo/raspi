FROM python:3.6

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV PYTHONPATH $PYTHONPATH:.

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g bower
