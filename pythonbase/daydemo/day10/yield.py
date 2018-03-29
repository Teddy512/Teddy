__author__ = "Alex Li"

import time
import queue
'''队列
带有 yield 的函数在 Python 中被称之为 generator（生成器）
使用yield实现协程操作例子

迭代器：for .. in .. 语法的叫做一个迭代器：
生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据:

mygenerator = (x*x for x in range(3))
for i in mygenerator :
    print(i)

#yield表达式可以接收send()发出的参数
'''

# 客户
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield   #yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)


# 生产
def producer():
    r = con.__next__()   #执行一步操作
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        time.sleep(1)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()

'''--->starting eating baozi...
--->starting eating baozi...

[c1] is eating baozi 1
[c2] is eating baozi 1
[producer] is making baozi 1

[c1] is eating baozi 2
[c2] is eating baozi 2
[producer] is making baozi 2

[c1] is eating baozi 3
[c2] is eating baozi 3
[producer] is making baozi 3

[c1] is eating baozi 4
[c2] is eating baozi 4
[producer] is making baozi 4

[c1] is eating baozi 5
[c2] is eating baozi 5
[producer] is making baozi 5
'''





