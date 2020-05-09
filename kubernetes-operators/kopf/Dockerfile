FROM python:3.7
COPY build /build
RUN pip install jinja2 && pip install kubernetes && pip install kopf
CMD kopf run /build/mysql-operator.py