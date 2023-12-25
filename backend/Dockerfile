FROM python:3.9
MAINTAINER Q9K
ENV PYTHONUNBUFFERED 1
ENV http_proxy "http://172.17.0.1:7890"
ENV HTTP_PROXY "http://172.17.0.1:7890"
ENV https_proxy "http://172.17.0.1:7890"
ENV HTTPS_PROXY "http://172.17.0.1:7890"
RUN mkdir /code
#COPY pip.conf /root/.pip/pip.conf
COPY NoBC-Academic-Backend /code
COPY uwsgi /code/uwsgi
COPY asgi /code/asgi
COPY start_uwsgi.sh /code/start_uwsgi.sh
#COPY supervisord.conf /code/supervisord.conf
COPY start_daphne.sh /code/start_daphne.sh
WORKDIR /code
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN pip install supervisor
RUN chmod +x start_daphne.sh
RUN chmod +x start_uwsgi.sh
EXPOSE 8000
