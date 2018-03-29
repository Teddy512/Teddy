# -*- coding: utf-8 -*-
# send

#！/esr/bin/env/ python

import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
# 声明queue
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='hello world')
print ("[x] Sent 'hello world'")

connection.close()









