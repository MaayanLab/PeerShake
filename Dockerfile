FROM debian:stable

RUN apt-get update && \
    apt-get -y install \
        nginx \
        python3 \
        python3-dev \
        python3-pip \
        python3-mysqldb \
        python3-setuptools \
        vim \
        uwsgi-core

ADD requirements.txt /requirements.txt
RUN pip3 install -Ivr /requirements.txt && \
    pip3 install -Iv uwsgi

ENV DEBUG 'false'
ENV BASE_URL '/peershake'
ENV SECRET_KEY 'secret'
ENV DATABASE_CONFIG '{"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}'
ENV SSL ''

VOLUME /ssl
EXPOSE 80
EXPOSE 443

ADD . /peershake
RUN chmod -R 777 /peershake
CMD /peershake/boot.sh
