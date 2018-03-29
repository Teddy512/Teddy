__author__ = "Alex Li"

import socket


# Socket Families(地址簇)
# socket.AF_UNIX unix本机进程间通信
# socket.AF_INET　IPV4　
# socket.AF_INET6  IPV6

# socket.SOCK_STREAM  #for tcp
# socket.SOCK_DGRAM   #for udp

# 将string中的数据发送到连接的套接字，
# 但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
# 内部通过递归调用send，将所有内容发送出去。

HOST = 'localhost'  # The remote host
PORT = 9999  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    s.sendall(msg)
    data = s.recv(1024)

    #
    print('Received', data)
s.close()
