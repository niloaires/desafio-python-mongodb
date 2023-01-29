FROM python:3.8
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y cron && touch /var/log/cron.log
RUN apt install python3-dev build-essential -y
RUN apt-get install default-libmysqlclient-dev
WORKDIR /app
COPY . .

ENV PYTHONUNBUFFERED=1

RUN pip3 install -r requeriments.txt

CMD python /app/manage.py runcrons
CMD python /app/manage.py runserver 0.0.0.0:8000
