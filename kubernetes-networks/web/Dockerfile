FROM nginx:1.17

COPY nginx.conf /etc/nginx/nginx.conf

RUN usermod -u 1001 nginx

RUN mkdir -p /var/run/nginx /app
RUN chown nginx:nginx /var/run/nginx /var/cache/nginx /app

EXPOSE 8000

USER 1001