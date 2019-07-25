FROM nginx:1.12.2-alpine

RUN mkdir /app

WORKDIR /app

RUN rm -f /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/nginx.conf

COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8000

USER 1001