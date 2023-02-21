## BUILDER ##

FROM python:3.8.9-alpine as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libc-dev linux-headers

RUN apk add jpeg-dev zlib-dev

RUN pip install --upgrade pip
#RUN pip install flake8
COPY . .
#RUN flake8 --ignore=E501,F401 .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

## FINAL ##

FROM python:3.8.9-alpine

# create directory for the app user
RUN mkdir -p /home

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home
ENV APP_HOME=/home/app
#RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy scripts
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

#RUN chown -R app:app /vol
RUN chmod -R 755 /vol/web

# chown all files to the app user
#RUN chown -R app:app $APP_HOME
#RUN chmod -R 755 $APP_HOME

# change app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/scripts/entrypoint.prod.sh"]
