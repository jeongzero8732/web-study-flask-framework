FROM python:3
COPY . /www
WORKDIR /www
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["uwsgi", "uwsgi.ini"]
