FROM nginx:1.12.2-alpine

RUN mkdir /app

COPY homework.html /app

COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8000

RUN chmod 777 /var/cache/nginx /var/run /var/log/nginx

RUN adduser skyline -u 1001 -D

RUN addgroup skyline root

USER 1001