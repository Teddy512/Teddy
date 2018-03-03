# -*- coding: utf-8 -*-
#    authon:teddy


'''反射




通过字符串映射或修改程序运行时的状态、属性、方法, 有以下4个方法'''

'''反射

python中的反射功能是由以下四个内置函数提供：
hasattr、getattr、setattr、delattr，改四个函数分别用于对对象内部执行：
检查是否含有某成员、获取成员、设置成员、删除成员。'''

def getattr(object, name, default=None): # known special case of getattr
    """
    getattr(object, name[, default]) -> value

    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.
    """
    pass



'判断object中有没有一个name字符串对应的方法或属性'



def setattr(x, y, v): # real signature unknown; restored from __doc__
    """
    Sets the named attribute on the given object to the specified value.

    setattr(x, 'y', v) is equivalent to ``x.y = v''''' """



def delattr(x, y): # real signature unknown; restored from __doc__

    """ Deletes the named attribute from the given object.

    delattr(x, 'y') is equivalent to ``del x.y'' """







class Foo(object):

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

obj = Foo()

# #### 检查是否含有成员 ####
hasattr(obj, 'name')
hasattr(obj, 'func')

# #### 获取成员 ####
getattr(obj, 'name')
getattr(obj, 'func')

# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)

# #### 删除成员 ####
delattr(obj, 'name')
delattr(obj, 'func')



'''详细解析：

当我们要访问一个对象的成员时，应该是这样操作：'''


class Foo(object):

    def __init__(self):
        self.name = 'alex'

    def func(self):
        return 'func'

obj = Foo()

# 访问字段
obj.name
# 执行方法
obj.func()



class Foo(object):

    def __init__(self):
        self.name = 'alex'

# 不允许使用 obj.name
obj = Foo()


'''答：有两种方式，如下：
复制代码'''

class Foo(object):

    def __init__(self):
        self.name = 'alex'

    def func(self):
        return 'func'

# 不允许使用 obj.name
obj = Foo()

print obj.__dict__['name']



class Foo(object):

    def __init__(self):
        self.name = 'alex'

    def func(self):
        return 'func'

# 不允许使用 obj.name
obj = Foo()

print getattr(obj, 'name')



'd、比较三种访问方式'

'''obj.name
    obj.__dict__['name']
    getattr(obj, 'name')'''


'''
那么问题来了？
a、上述访问对象成员的 name 和 func 是什么？
答：是变量名
b、obj.xxx 是什么意思？
答：obj.xxx 表示去obj中或类中寻找变量名 xxx，并获取对应内存地址中的内容。
c、需求：请使用其他方式获取obj对象中的name变量指向内存中的值 “alex”'''

import importlib

__import__('import_lib.metaclass') #这是解释器自己内部用的
#importlib.import_module('import_lib.metaclass') #与上面这句效果一样，官方建议用这个





































