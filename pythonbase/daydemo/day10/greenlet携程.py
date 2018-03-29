


'''
　　Greenlet是python的一个C扩展，来源于Stackless python，旨在提供可自行调度的‘微线程’，
即协程。generator实现的协程在yield value时只能将value返回给调用者(caller)。 而在greenlet中，
target.switch（value）可以切换到指定的协程（target）， 然后yield value。greenlet用switch来表示协程的切换，
从一个协程切换到另一个协程需要显式指定。
greenlet的安装很简单：pip install greenlet 即可，安装好了之后我们来看一个官方的例子'''

from greenlet import greenlet
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1) #启动一个携程
gr2 = greenlet(test2)
gr1.switch()


'''当创建一个greenlet时
，首先初始化一个空的栈， switch到这个栈的时候，
会运行在greenlet构造时传入的函数（首先在test1中打印 12），
 如果在这个函数（test1）中switch到其他协程（到了test2 打印34），
那么该协程会被挂起，等到切换回来（在test2中切换回来 打印34）。
当这个协程对应函数执行完毕，那么这个协程就变成dead状态。'''

'''　
　比较重要的几个属性：

　　run：当greenlet启动的时候会调用到这个callable，如果我们需要继承greenlet.greenlet时，需要重写该方法

　　switch：前面已经介绍过了，在greenlet之间切换

　　parent：可读写属性，后面介绍

　　dead：如果greenlet执行结束，那么该属性为true

　　throw：切换到指定greenlet后立即跑出异常

'''

'''使用greenlet需要注意一下三点：

　　第一：greenlet创生之后，一定要结束，不能switch出去就不回来了，否则容易造成内存泄露

　　第二：python中每个线程都有自己的main greenlet及其对应的sub-greenlet ，不能线程之间的greenlet是不能相互切换的

　　第三：不能存在循环引用，这个是官方文档明确说明
'''

from greenlet import greenlet, GreenletExit
huge = []
def show_leak():
    def test1():
        gr2.switch()

    def test2():
        huge.extend([x* x for x in range(100)])
        gr1.switch()
        print 'finish switch del huge'
        del huge[:]

    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()
    gr1 = gr2 = None
    print 'length of huge is zero ? %s' % len(huge)

if __name__ == '__main__':
    show_leak()

'''　在test2函数中 第11行，我们将huge清空，然后再第16行将gr1、gr2的引用计数降到了0。但运行结果告诉我们，
第11行并没有执行，所以如果一个协程没有正常结束是很危险的，往往不符合程序员的预期。greenlet提供了解决这个问题的办法，
官网文档提到：如果一个greenlet实例的引用计数变成0，
那么会在上次挂起的地方抛出GreenletExit异常，这就使得我们可以通过try ... finally 处理资源泄露的情况。如下面的代码：'''

from greenlet import greenlet, GreenletExit
huge = []
def show_leak():
    def test1():
        gr2.switch()

    def test2():
        huge.extend([x* x for x in range(100)])
        try:
            gr1.switch()
        finally:
            print 'finish switch del huge'
            del huge[:]

    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()
    gr1 = gr2 = None
    print 'length of huge is zero ? %s' % len(huge)

if __name__ == '__main__':
    show_leak()
'''上述代码的switch流程：main greenlet --> gr1 --> gr2 --> gr1 --> main greenlet,
很明显gr2没有正常结束（在第10行刮起了）。第18行之后gr1,gr2的引用计数都变成0，
那么会在第10行抛出GreenletExit异常，因此finally语句有机会执行。同时，
在文章开始介绍Greenlet module的时候也提到了，GreenletExit这个异常并不会抛出到parent，所以main greenlet也不会出异常。

　　看上去貌似解决了问题，但这对程序员要求太高了，百密一疏。所以最好的办法还是保证协程的正常结束。

总结：
　　之前的文章其实已经提到提到了coroutine协程的强大之处，对于异步非阻塞，而且还需要保留上下文的场景非常适用
。greenlet跟强大，可以从一个协程切换到任意其他协程，这是generator做不到的，但这种能力其实也是双刃剑，前面的注意事项也提到了
，必须保证greenlet的正常结束，在协程之间任意的切换很容易出问题。

　　比如对于服务之间异步请求的例子，简化为服务A的一个函数foo需要异步访问服务B，可以这样封装greenlet：用decorator装饰函数foo，
当调用这个foo的时候建立一个greenlet实例，并为这个greenley对应一个唯一的gid，在foo方法发出异步请求
（写到gid）之后，switch到parent，这个时候这个新的协程处于挂起状态。当请求返回之后，通过gid找到之前被挂起的协程，恢复该协程即可。
More simple More safety，保证旨在main和一级子协程之间切换。需要注意的是处理各种异常 以及请求超时的情况，避免内存泄露
，gvent对greenlet的使用大致也是这样的。

'''