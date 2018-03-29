

import sys
import socket
import time
import gevent

'''当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，
等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，
有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。



由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，
这一过程在启动时通过monkey patch完成：'''

from gevent import socket, monkey

monkey.patch_all()

'''tcpip  socket-->bind-->listen'''
def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)


def handle_request(conn):   #获取一个请求
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)  #如果没有数据就关闭连接
    except Exception as  ex:
        print(ex)
    finally:
        conn.close()   #关闭连接


if __name__ == '__main__':
    server(8001)   #启动


'''
SHUT_RD：关闭连接的读端。也就是该套接字不再接受数据，任何当前在套接字接受缓冲区的数据将被丢弃。进程将不能对该
    套接字发出任何读操作。对TCP套接字该调用之后接受到的任何数据将被确认然后无声的丢弃掉。
    SHUT_WR:关闭连接的写端，进程不能在对此套接字发出写操作
    SHUT_RDWR:相当于调用shutdown两次：首先是以SHUT_RD,然后以SHUT_WR


使用close中止一个连接，但它只是减少描述符的参考数，并不直接关闭连接，只有当描述符的参考数为0时才关闭连接。
shutdown可直接关闭描述符，不考虑描述符的参考数，可选择中止一个方向的连接。'''
'''
expect中最关键的四个命令是send,expect,spawn,interact。


send：用于向进程发送字符串
expect：从进程接收字符串
spawn：启动新的进程
interact：允许用户交互


常用expect命令
expect中命令是最重要的部分，它们完成Expect中最关键的功能
，命令使用的特点就是他们本身就可以单独执行，使用上类似于：
命令 [选项] 参数


 spawn
spawn命令是Expect的初始命令，它用于启动一个进程，
之后所有expect操作都在这个进程中进行，如果没有spawn语句，
整个expect就无法再进行下去了，使用方法就像下面这样：

'''

























