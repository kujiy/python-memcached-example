FROM python:3
RUN apt-get update && apt-get install -y memcached python-memcache  python3-memcache netcat libmemcached-dev libmemcached-tools && pip install python-memcached
ENV PATH="/usr/share/memcached/scripts/:${PATH}" 
