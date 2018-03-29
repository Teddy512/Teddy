#authon :teddy
import redis

r=redis.Redis(host='127.0.0.1',port=6379)
r.set("teddy",'name')
print r.get('teddy')







'''管道

redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作'''

import redis

pool=redis.ConnectionPool(host='127.0.0.1',port=6379)
r=redis.Redis(connection_pool=pool)
pipe=r.pipeline(transaction=True)

# 他两是最后一起执行
pipe.set('name','teddy')
pipe.set('role','sb')



pipe.execute()


