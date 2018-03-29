__author__ = "Alex Li"


'''

Paramiko

　　paramiko模块，基于SSH用于连接远程服务器并执行相关操作'''


import paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.168.1.142', port=52113, username='root', password='123456')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
res,err = stdout.read(),stderr.read()
result = res if res else err

print(result.decode())

# 关闭连接
ssh.close()

