__author__ = "Alex Li"
import socket
client = socket.socket()

#client.connect(('192.168.16.200',9999))
client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()  #strip() 方法用于移除字符串头尾指定的字符
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024) ##接受命令结果的长度
    # recv{接受套接字的数据。数据以字符串形式返回
    # ，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略}
    print("命令结果大小:",cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()) :
        data = client.recv(1024)
        received_size += len(data) #每次收到的有可能小于1024，所以必须用len判断
        #print(data.decode())
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())


client.close()

# decode的作用是将其他编码的字符转换成unicode编码
# ,如str1,decode('gb2312'),表示将gb2312编码的字符串str1转换成unicode编码。
# encode的作用是将unicode编码转换成其他编码的字符串,
# 如str2,encode('gb2312'),表示将unicode编码的字符串str2转换成gb2312






































