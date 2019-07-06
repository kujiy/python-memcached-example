version: '3.4'

#1version: '2'

services:
  memcached:
    image: 'memcached'
    container_name: mem
    ports:
      - '11211:11211'
    networks:
      - network1

  py:
    image: python:3
    build:
      context: .
    ports:
      - 88:80
    networks:
      - network1

networks:
  network1:
    internal: true
