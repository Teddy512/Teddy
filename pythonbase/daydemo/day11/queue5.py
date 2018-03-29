'更细致的消息过滤'


'''尽管使用直接交换改进了我们的系统，但它仍然有局限性 - 它不能根据多个标准进行路由。

在我们的日志系统中，我们可能不仅需要根据严重性来订阅日志，还要根据发布日志的来源进行订阅。
您可能从syslog unix工具知道这个概念，该工具根据严重性（信息/警告/暴击...）和工具（auth / cron / kern ...）来路由日志。

这会给我们很大的灵活性 - 我们可能想听取来自'cron'的严重错误，而且还听取来自'kern'的所有日志。'''



'publisher'
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
 #有选择的将接受消息
channel.exchange_declare(exchange='topic_logs',type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='topic_logs',routing_key=routing_key,  body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()





'subscriber'
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()