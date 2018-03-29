import selectors
import socket



'''Python/ selectors模块及队列
Python/selectors模块及队列
 selectors模块是可以实现IO多路复用机制：

它具有根据平台选出最佳的IO多路机制，比如在win的系统上他默认的是select模式而在linux上它默认的epoll。
常用共分为三种：
select、poll、epoll

select的缺点：
1、每次调用都要将所有的文件描述符（fd）拷贝的内核空间，导致效率下降
2、遍历所有的文件描述符（fd）查看是否有数据访问
3、最大链接数限额（1024）


poll：
它就是select和epoll的过渡阶段，它没有最大链接数的限额


epoll：
1、第一个函数是创建一个epoll句柄，将所有的描述符（fd）拷贝到内核空间，但只拷贝一次。

2、回调函数，某一个函数或某一个动作成功完成之后会触发的函数为所有的描述符（fd）绑定一个回调函数，一旦有数据访问就是触发该回调函数，回调函数将（fd）放到链表中

3、函数判断链表是否为空

4、最大启动项没有限额

'''


sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr,mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read) #新连接注册read回调函数


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select() #默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data #accept
        callback(key.fileobj, mask) #key.fileobj=  文件句柄








