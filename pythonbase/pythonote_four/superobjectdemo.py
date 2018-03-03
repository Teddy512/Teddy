# -*- coding: utf-8 -*-
#    authon:teddy




'''类的特殊成员方法
1. __doc__　　表示类的描述信息'''

class Foo:
    """ 描述类信息，这是用于看片的神奇 """

    def func(self):
        pass

print Foo.__doc__
#输出：类的描述信息



'''2. __module__ 和  __class__

　　__module__ 表示当前操作的对象在那个模块

　　__class__     表示当前操作的对象的类是什么'''

'lib\aa.py'
class C:

    def __init__(self):
        self.name = 'wupeiqi'


'index.py'


'from lib.aa import C'

obj = C()
print obj.__module__  # 输出 lib.aa，即：输出模块
print obj.__class__      # 输出 lib.aa.C，即：输出类




'''3. __init__ 构造方法，通过类创建对象时，自动触发执行。
4.__del__

　析构方法，当对象在内存中被释放时，自动触发执行。

    注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，
    因为此工作都是交给Python解释器来执行，所以，析构函数的调用是由解释器在进行垃圾回收时自动触发执行的

　　

 5. __call__ 对象后面加括号，触发执行。

    注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；
    而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()

'''
class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):

        print '__call__'


obj = Foo() # 执行 __init__
obj()       # 执行 __call_


'6. __dict__ 查看类或对象中的所有成员 　　'


class Province:

    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print 'func'

# 获取类的成员，即：静态字段、方法、
print Province.__dict__
# 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': None}

obj1 = Province('HeBei',10000)
print obj1.__dict__
# 获取 对象obj1 的成员
# 输出：{'count': 10000, 'name': 'HeBei'}

obj2 = Province('HeNan', 3888)
print obj2.__dict__
# 获取 对象obj1 的成员
# 输出：{'count': 3888, 'name': 'HeNan'}





'7.__str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。'

class Foo:

    def __str__(self):
        return 'alex li'


obj = Foo()
print obj
# 输出：alex li



'8.__getitem__、__setitem__、__delitem__'

'用于索引操作，如字典。以上分别表示获取、设置、删除数据'


class Foo(object):

    def __getitem__(self, key):
        print('__getitem__',key)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)

    def __delitem__(self, key):
        print('__delitem__',key)


obj = Foo()

result = obj['k1']      # 自动触发执行 __getitem__
obj['k2'] = 'alex'   # 自动触发执行 __setitem__
del obj['k1']



'9. __new__ \ __metaclass__'


class Foo(object):


    def __init__(self,name):
        self.name = name


f = Foo("alex")

'''上述代码中，obj 是通过 Foo 类实例化的对象，其实，不仅 obj 是一个对象，Foo类本身也是一个对象，因为在Python中一切事物都是对象。

如果按照一切事物都是对象的理论：obj对象是通过执行Foo类的构造方法创建，那么Foo类对象应该也是通过执行某个类的 构造方法 创建。'''

print type(f) # 输出：<class '__main__.Foo'>     表示，obj 对象由Foo类创建
print type(Foo) # 输出：<type 'type'>              表示，Foo类对象由 type 类创建

'''所以，f对象是Foo类的一个实例，Foo类对象是 type 类的一个实例，即：Foo类对象 是通过type类的构造方法创建。

那么，创建类就可以有两种方式：'''

'a). 普通方式 '

class Foo(object):

    def func(self):
        print 'hello alex'

'b). 特殊方式'

def func(self):
    print 'hello wupeiqi'

Foo = type('Foo',(object,), {'func': func})
#type第一个参数：类名
#type第二个参数：当前类的基类
#type第三个参数：类的成员


def func(self):
    print("hello %s"%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age
Foo = type('Foo',(object,),{'func':func,'__init__':__init__})

f = Foo("jack",22)
f.func()



'''类 是由 type 类实例化产生

那么问题来了，类默认是由 type 类实例化产生，type类中如何实现的创建类？类又是如何创建对象？

答：类中有一个属性 __metaclass__，其用来表示该类由 谁 来实例化创建，所以，我们可以为 __metaclass__
设置一个type类的派生类，从而查看 类 创建的过程。'''


'please  see view image'

#
# class MyType(type):
#     def __init__(self,*args,**kwargs):
#
#         print("Mytype __init__",*args,**kwargs)
#
#     def __call__(self, *args, **kwargs):
#         print("Mytype __call__", *args, **kwargs)
#         obj = self.__new__(self)
#         print("obj ",obj,*args, **kwargs)
#         print(self)
#         self.__init__(obj,*args, **kwargs)
#         return obj
#
#     def __new__(cls, *args, **kwargs):
#         print("Mytype __new__",*args,**kwargs)
#         return type.__new__(cls, *args, **kwargs)
#
# print('here...')
# class Foo(object,metaclass=MyType):
#
#
#     def __init__(self,name):
#         self.name = name
#
#         print("Foo __init__")
#
#     def __new__(cls, *args, **kwargs):
#         print("Foo __new__",cls, *args, **kwargs)
#         return object.__new__(cls)
#
# f = Foo("Alex")
# print("f",f)
# print("fname",f.name)

'自定义元类 类的生成 调用 顺序依次是 __new__ --> __init__ --> __call__'''


