FROM python:3.8.9-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libc-dev linux-headers

RUN apk add jpeg-dev zlib-dev libjpeg

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir /app
COPY . /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

#RUN adduser -S user

#RUN chown -R user /vol

RUN chmod -R 755 /vol/web
#RUN chown -R user /app
#RUN chmod -R 755 /app

#USER user

CMD python manage.py makemigrations; python manage.py migrate;
ENTRYPOINT ["/scripts/entrypoint.sh"]
