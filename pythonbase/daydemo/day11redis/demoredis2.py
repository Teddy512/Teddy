#teddy    redis

import redis
class RedisHelper:
      def _init__(self):
          self.__conn=redis.Redis(host='127.0.0.10',port=6379)   #连接host
          self.chan_sub='fm104.5'
          self.chan_pub='fm104.5'


      def public(self,msg):
          self.__conn.publish(self.chan_pub,msg)
          return True

      def subscrible(self):
          pub=self.__conn.pubsub()
          pub.subscribe(self.chan_sub)
          pub.parse_response()
          return pub


      