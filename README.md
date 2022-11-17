# python-script-to-check-rabbitmq-access
This template contains a python script to test RabbitMQ access on a given broker_url.

* RabbitMQ
  - It is an Open Source message broker.
  - It is lightweight and easy to deploy on prem as well as in cloud.
  - It supports multiple messaging protocols like AMQP, HTTP etc.
  - It can run on multiple OS and cloud environments.
  - It also provides wide range of developer tools for multiple languages.

* broker_url
  - It is the URL location of the broker instance we want to use.
  - Sample broker URL example : 
      - A sample broker_url looks like this -> "amqp://user:password@remote.server.com:port//vhost"
  
* Understanding imports
  - pika
    - Pika is a pure-Python implementation of the AMQP 0-9-1 protocol including RabbitMQ’s extensions.
  - re
    - This is a built-in python package for Regular Expressions.

- Prerequisites
  - a working broker_url.
  - Python installed.

* How to Use?
  - python3 checkRabbitMQConnection.py
  
