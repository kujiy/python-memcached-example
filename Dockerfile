FROM python:3
RUN apt-get update && apt-get install -y net-tools dnsutils memcached python-memcache  python3-memcache netcat libmemcached-dev libmemcached-tools 
ENV PATH="/usr/share/memcached/scripts/:${PATH}" 
COPY ./app /app
RUN ls /app
WORKDIR /app
RUN pip install -r requirements.txt
