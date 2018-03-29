# 订阅者：


from monitor.RedisHelper  import RedisHelper

obj=RedisHelper()
redis_sub=obj.subscribe()
while True:
      msg=redis_sub.parse_response()
      print msg






# 发布者

from monitor.RedisHelper  import RedisHelper

obj=RedisHelper()
obj.public('hello')