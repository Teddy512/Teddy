# -*- coding: utf-8 -*-
#    authon:teddy

'其他相关'

'''一、isinstance(obj, cls)

 检查是否obj是否是类 cls 的对象'''


class Foo(object):
    pass

obj = Foo()

isinstance(obj, Foo)




'''二、issubclass(sub, super)

检查sub类是否是 super 类的派生类'''

class Foo(object):
    pass

class Bar(Foo):
    pass

issubclass(Bar, Foo)




'''
三、异常处理

1、异常基础

在编程过程中为了增加友好性，在程序出现bug时一般不会将错误信息显示给用户，而是现实一个提示的页面，通俗来说就是不让用户看见大黄页！！！

	'''
try:
    pass
except Exception,ex:
    pass

# example1

while True:
    num1 = raw_input('num1:')
    num2 = raw_input('num2:')
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
    except Exception, e:
        print '出现异常，信息如下：'
        print e




'''
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
 '''


'one:'

dic = ["wupeiqi", 'alex']
try:
    dic[10]
except IndexError, e:
    print e



'two'
dic = {'k1':'v1'}
try:
    dic['k20']
except KeyError, e:
    print e



'three'

s1 = 'hello'
try:
    int(s1)
except ValueError, e:
    print e




'万能异常 在python的异常中，有一个万能异常：Exception，他可以捕获任意异常，即：'


s1 = 'hello'
try:
    int(s1)
except Exception,e:
    print e



'3、异常其他结构'


try:
    # 主代码块
    pass
except KeyError,e:
    # 异常时，执行该块
    pass
else:
    # 主代码块执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass



'4、主动触发异常'


try:
    raise Exception('错误了。。。')
except Exception,e:
    print e

'5、自定义异常'


class WupeiqiException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise WupeiqiException('我的异常')
except WupeiqiException,e:
    print e





'6、断言'


# assert 条件

assert 1 == 1

assert 1 == 2