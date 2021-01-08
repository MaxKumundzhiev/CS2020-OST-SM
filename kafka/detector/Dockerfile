# docker-compose.yml
FROM python:3.6

WORKDIR /usr/src/app

ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD . ./

CMD ["python", "app.py"]