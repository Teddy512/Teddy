# -*- coding: utf-8 -*-
#    authon:teddy

'''
设计模式

一、单例模式

单例，顾名思义单个实例。

    学习单例之前，首先来回顾下面向对象的内容：

    python的面向对象由两个非常重要的两个“东西”组成：类、实例

    面向对象场景一：

    如：创建三个游戏人物，分别是：

        苍井井，女，18，初始战斗力1000
        东尼木木，男，20，初始战斗力1800
        波多多，女，19，初始战斗力2500'''







class Person:

      def __init__(self, na, gen, age, fig):
        self.name = na
        self.gender = gen
        self.age = age
        self.fight =fig

      def grassland(self):
          self.fight=self.fight-200


' 创建实例  '


cang = Person('井井', '女', 18, 1000)    # 创建苍井井角色
dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
bo = Person('多多', '女', 19, 2500)      # 创建波多多角色



'''面向对象场景二：

如：创建对数据库操作的公共类

    增
    删
    改
    查'''


class DbHelper(object):
      def __init__(self):
          self.hostname='1.1.1.1'
          self.port=3306
          self.password='pwd'
          self.username='root'


      def fetch(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

      def create(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

      def remove(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

      def modify(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

# #### 操作类 ####

db = DbHelper()
db.create()








'实例：结合场景二实现Web应用程序'

from wsgiref.simple_server import make_server


class DbHelper(object):

    def __init__(self):
        self.hostname = '1.1.1.1'
        self.port = 3306
        self.password = 'pwd'
        self.username = 'root'

    def fetch(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        return 'fetch'

    def create(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        return 'create'

    def remove(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        return 'remove'

    def modify(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        return 'modify'


class Handler(object):

    def index(self):
        # 创建对象
        db = DbHelper()
        db.fetch()
        return 'index'

    def news(self):
        return 'news'


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    temp = url.split('/')[1]
    obj = Handler()
    is_exist = hasattr(obj, temp)
    if is_exist:
        func = getattr(obj, temp)
        ret = func()
        return ret
    else:
        return '404 not found'


if __name__ == '__main__':
    httpd = make_server('', 8001, RunServer)
    print "Serving HTTP on port 8001..."
    httpd.serve_forever()




'''对于上述实例，每个请求到来，都需要在内存里创建一个实例，再通过该实例执行指定的方法。

那么问题来了...如果并发量大的话，内存里就会存在非常多功能上一模一样的对象。
存在这些对象肯定会消耗内存，对于这些功能相同的对象可以在内存中仅创建一个，需要时都去调用，也是极好的！！！

单例模式出马，单例模式用来保证内存中仅存在一个实例！！！

通过面向对象的特性，构造出单例模式：'''

# ########### 单例类定义 ###########
class Foo(object):

    __instance = None

    @staticmethod
    def singleton():
        if Foo.__instance:
            return Foo.__instance
        else:
            Foo.__instance = Foo()
            return Foo.__instance

# ########### 获取实例 ###########
obj = Foo.singleton()

'对于Python单例模式，创建对象时不能再直接使用：obj = Foo()，而应该调用特殊的方法：obj = Foo.singleton() 。'


from wsgiref.simple_server import make_server

# ########### 单例类定义 ###########
class DbHelper(object):

    __instance = None

    def __init__(self):
        self.hostname = '1.1.1.1'
        self.port = 3306
        self.password = 'pwd'
        self.username = 'root'

    @staticmethod
    def singleton():
        if DbHelper.__instance:
            return DbHelper.__instance
        else:
            DbHelper.__instance = DbHelper()
            return DbHelper.__instance

    def fetch(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

    def create(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

    def remove(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass

    def modify(self):
        # 连接数据库
        # 拼接sql语句
        # 操作
        pass


class Handler(object):

    def index(self):
        obj =  DbHelper.singleton()
        print id(single)
        obj.create()
        return 'index'

    def news(self):
        return 'news'


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    temp = url.split('/')[1]
    obj = Handler()
    is_exist = hasattr(obj, temp)
    if is_exist:
        func = getattr(obj, temp)
        ret = func()
        return ret
    else:
        return '404 not found'

if __name__ == '__main__':
    httpd = make_server('', 8001, RunServer)
    print "Serving HTTP on port 8001..."
    httpd.serve_forever()


'总结：单利模式存在的目的是保证当前内存中仅存在单个实例，避免内存浪费！！！'


















