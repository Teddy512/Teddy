#-*-coding:utf-8 -*-


'''
pip install pika
'''
import  pika
connection=pika.BlockingConnection(pika.ConnectionParamenters('localhost'))
channel=connection.channel()

def callback(ch,method,properties,body):
    print ("[x] Received %r"  %body)
channel.basic_consume(callback(queue='hello',no_ack=True))
print ('[*] waiting for messages.To  exit pressCTRL+C  ')
channel.start_consuming()






import pika, time

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))


channel = connection.channel()  #'Channel:进行消息读写的通道；'


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(20)
    print(" [x] Done")
    print("method.delivery_tag",method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                      queue='task_queue',
                      no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



























'''有选择的接收消息(exchange type=direct)　start

RabbitMQ还支持根据关键字发送，即：队列绑定关键字，发送者将数据根据关键字发送到消息exchange，exchange根据
关键字 判定应该将数据发送至指定队列。'''
'''send端'''
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()



'''receive端'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')


result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):#回调函数
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True ) #不确认)

channel.start_consuming()

'''有选择的接收消息(exchange type=direct)　ending '''