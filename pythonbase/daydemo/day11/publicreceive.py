'''Publish\Subscribe(消息发布\订阅)　

之前的例子都基本都是1对1的消息发送和接收，即消息只能发送到指定的queue里，但有些时候你想让你的消息被所有的Queue收到，类似广播的效果，这时候就要用到exchange了，

An exchange is a very simple thing. On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives. Should it be appended to a particular queue? Should it be appended to many queues? Or should it get discarded. The rules for that are defined by the exchange type.

Exchange在定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接收消息


fanout: 所有bind到此exchange的queue都可以接收消息
direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
topic:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息

　　 表达式符号说明：#代表一个或多个字符，*代表任何字符
      例：#.a会匹配a.a，aa.a，aaa.a等
          *.a会匹配a.a，b.a，c.a等
     注：使用RoutingKey为#，Exchange Type为topic的时候相当于使用fanout　

headers: 通过headers 来决定把消息发给哪些queue'''




'消息pub lisher'
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()










'消息sub  scriber'
#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

result = channel.queue_declare(exclusive=True) #不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()