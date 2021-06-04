#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# It's okay to run following two flush and migrate command on development mode.. when debug mode is 1 not recommended
# for production:

# python manage.py flush --no-input
# python manage.py migrate


#uwsgi --socket :8000 --master --enable-threads --module personal.wsgi

exec "$@"

