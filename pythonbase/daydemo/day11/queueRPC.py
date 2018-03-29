''
'''Remote procedure call (RPC)

To illustrate how an RPC service could be used we're going to create a simple client class. It's going to expose a
method named call which sends an RPC request and blocks until the answer is received:'''

'''远程过程调用（RPC）

为了说明如何使用RPC服务，我们将创建一个简单的客户端类。 它将公开一个名为call的方法，它发送一个RPC请求并阻塞，直到收到答案：
fibonacci_rpc = FibonacciRpcClient()
result = fibonacci_rpc.call(4)
print("fib(4) is %r" % result)

'''

'''
Exchange:交换机，决定了消息路由规则；
Queue:消息队列；
Channel:进行消息读写的通道；
Bind:绑定了Queue和Exchange，意即为符合什么样路由规则的消息，将会放置入哪一个消息队列；'''

'''消息队列的使用过程大概如下：
（1）客户端连接到消息队列服务器，打开一个channel。
　　（2）客户端声明一个exchange，并设置相关属性。
　　（3）客户端声明一个queue，并设置相关属性。
　　（4）客户端使用routing key，在exchange和queue之间建立好绑定关系。
　　（5）客户端投递消息到exchange。'''


'RPC server'


#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import pika
import time


#固定用法  用于连接（1）客户端连接到消息队列服务器，打开一个channel。
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

 # 声明一个queue
channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)
    ch.basic_publish(exchange='',routing_key=props.reply_to,properties=pika.BasicProperties(correlation_id =props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()








'RPC client'
import pika
import uuid

class FibonacciRpcClient(object):
    # 构造函数，实例化变量
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)


