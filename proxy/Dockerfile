FROM nginxinc/nginx-unprivileged:1-alpine


COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY uwsgi_params /etc/nginx/uwsgi_params


#USER root
#
#
#RUN mkdir -p /vol/static
#RUN chmod 755 /vol/static
#
#USER nginx



#server {
#    listen 80;
#
#    location /static {
#        alias /vol/static;
#    }
#
#    location / {
#        uwsgi_pass app:8000;
#        include /etc/nginx/uwsgi_params;
#    }
#}
