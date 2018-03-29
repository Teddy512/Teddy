'''在这种模式下，RabbitMQ会默认把p发的消息依次分发给各个消费者(c),跟负载均衡差不多


Work Queues

'''
'''消息提供者代码'''

import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='task_queue')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
import sys

message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      )
                      )
print(" [x] Sent %r" % message)
connection.close()







'''消费者代码'''

import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='task_queue')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
import sys

message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()
channel.basic_publish(exchange='',routing_key='task_queue',body=message,properties=pika.BasicProperties(delivery_mode=2,  # make message persistent
                      )
                      )
print(" [x] Sent %r" % message)
connection.close()
