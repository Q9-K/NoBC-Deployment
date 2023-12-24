FROM python:3.9
MAINTAINER Q9K
ENV PYTHONUNBUFFERED 1
COPY pip.conf /root/.pip/pip.conf
RUN mkdir -p /code
ADD ./code /code
COPY ./uwsgi /code/uwsgi
COPY ./asgi /code/asgi
COPY start_uwsgi.sh /code/start_uwsgi.sh
COPY supervisord.conf /code/supervisord.conf
COPY start_daphne.sh /code/start_daphne.sh
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN pip install supervisor
RUN chmod +x start_daphne.sh
RUN chmod +x start_uwsgi.sh
EXPOSE 8000
