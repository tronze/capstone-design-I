# WingIt Application
FROM python:3.11

RUN mkdir /code

WORKDIR /code

ADD . /code

RUN pip3 install -r /code/requirements.txt

RUN ["chmod", "+x", "./run.sh"]

ENTRYPOINT ["sh","./run.sh"]