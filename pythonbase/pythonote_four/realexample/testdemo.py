# -*- coding: utf-8 -*-
#    authon:teddy



import sys


def s1():
    print 's1'


def s2():
    print 's2'


this_module = sys.modules[__name__]

hasattr(this_module, 's1')
getattr(this_module, 's2')





'类也是对象'


class Foo(object):

    staticField = "old boy"

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'

print getattr(Foo, 'staticField')
print getattr(Foo, 'func')
print getattr(Foo, 'bar')