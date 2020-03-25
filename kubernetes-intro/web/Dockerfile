FROM nginx:1.16.1
USER 1001
RUN useradd -u 1001 pathfinder

RUN chmod u+s /usr/sbin/nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY homework.html /app/homework.html

ENTRYPOINT ["nginx", "-g", "daemon off;"]
EXPOSE 8000/tcp