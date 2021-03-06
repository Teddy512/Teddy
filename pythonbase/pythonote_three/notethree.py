# -*- coding: utf-8 -*-
#    authon:teddy


'''本节内容

    迭代器&生成器
    装饰器
    Json & pickle 数据序列化
    软件目录结构规范
    作业:ATM项目开发'''


'''1.列表生成式，迭代器&生成器
列表生成式

孩子，我现在有个需求，看列表[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],我要求你把列表里的每个值加1，你怎么实现？你可能会想到2种方式 
普通青年版
复制代码'''

a = [1,3,4,6,7,7,8,9,11]

for index,i in enumerate(a):
    a[index] +=1
print(a)


'''
a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = map(lambda x:x+1, a)
a
<map object at 0x101d2c630>
for i in a:print(i)
'''


'其实还有一种写法，如下 '

a = [i+1 for i in range(10)]
a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



'''生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：'''

	
L = [x * x for x in range(10)]
L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
g
'<generator object <genexpr> at 0x1022ef630>'

'''创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：'''

	
next(g)
0
next(g)
1
next(g)


'''我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：'''

14
	
g = (x * x for x in range(10))
for n in g:
   print(n)

0
1
4
9
16
25
36
49
64
81

 

'''所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：'''

	
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

'注意，赋值语句：'
1
	
# a, b = b, a + b

'相当于：'

	
# t = (b, a + b) '
# a = t[0]
# b = t[1]

'但不必显式写出临时变量t就可以赋值。'

'上面的函数可以输出斐波那契数列的前N个数：'

	
'''fib(10)
done

仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：'''


def fib(max):
    n,a,b = 0,0,1

    while n < max:
        #print(b)
        yield  b
        a,b = b,a+b

        n += 1

    return 



'''但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：'''

	
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

'''
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done'''



# '还可通过yield实现在单线程的情况下实现并发运算的效果'　
import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")



'''迭代器

我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：'''


from collections import Iterable
isinstance([], Iterable)
True
isinstance({}, Iterable)
True
isinstance('abc', Iterable)
True
isinstance((x for x in range(10)), Iterable)
True
isinstance(100, Iterable)
False

'''而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

*可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：'''

	
from collections import Iterator
isinstance((x for x in range(10)), Iterator)
True
isinstance([], Iterator)
False
isinstance({}, Iterator)
False
isinstance('abc', Iterator)
False

'''生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：'''

	
isinstance(iter([]), Iterator)
True
isinstance(iter('abc'), Iterator)
True

'''你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

 

小结

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：'''

	
for x in [1, 2, 3, 4, 5]:
    pass

'实际上完全等价于：'


# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break







 





