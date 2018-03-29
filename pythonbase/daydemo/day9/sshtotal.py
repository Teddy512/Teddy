__author__ = "teddy"

'''一、安装

1 pip3 install paramiko

二、使用

SSHClient

用于连接远程服务器并执行基本命令'''


'example1'
'基于用户名密码连接：'
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', password='123')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')
# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()





import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', password='123')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
print stdout.read()

transport.close()

'''SSHClient 封装 Transport
'''


'例二：example1'
# 基于公钥密钥连接：
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', key=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()



import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')

transport.close()

'SSHClient 封装 Transport'

'SSHClient 封装 Transport'








import paramiko
from io import StringIO

key_str = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAq7gLsqYArAFco02/55IgNg0r7NXOtEM3qXpb/dabJ5Uyky/8
NEHhFiQ7deHIRIuTW5Zb0kD6h6EBbVlUMBmwJrC2oSzySLU1w+ZNfH0PE6W6fans
H80whhuc/YgP+fjiO+VR/gFcqib8Rll5UfYzf5H8uuOnDeIXGCVgyHQSmt8if1+e
7hn1MVO1Lrm9Fco8ABI7dyv8/ZEwoSfh2C9rGYgA58LT1FkBRkOePbHD43xNfAYC
tfLvz6LErMnwdOW4sNMEWWAWv1fsTB35PAm5CazfKzmam9n5IQXhmUNcNvmaZtvP
c4f4g59mdsaWNtNaY96UjOfx83Om86gmdkKcnwIDAQABAoIBAQCnDBGFJuv8aA7A
ZkBLe+GN815JtOyye7lIS1n2I7En3oImoUWNaJEYwwJ8+LmjxMwDCtAkR0XwbvY+
c+nsKPEtkjb3sAu6I148RmwWsGncSRqUaJrljOypaW9dS+GO4Ujjz3/lw1lrxSUh
IqVc0E7kyRW8kP3QCaNBwArYteHreZFFp6XmtKMtXaEA3saJYILxaaXlYkoRi4k8
S2/K8aw3ZMR4tDCOfB4o47JaeiA/e185RK3A+mLn9xTDhTdZqTQpv17/YRPcgmwz
zu30fhVXQT/SuI0sO+bzCO4YGoEwoBX718AWhdLJFoFq1B7k2ZEzXTAtjEXQEWm6
01ndU/jhAasdfasdasdfasdfa3eraszxqwefasdfadasdffsFIfAsjQb4HdkmHuC
OeJrJOd+CYvdEeqJJNnF6AbHyYHIECkj0Qq1kEfLOEsqzd5nDbtkKBte6M1trbjl
HtJ2Yb8w6o/q/6Sbj7wf/cW3LIYEdeVCjScozVcQ9R83ea05J+QOAr4nAoGBAMaq
UzLJfLNWZ5Qosmir2oHStFlZpxspax/ln7DlWLW4wPB4YJalSVovF2Buo8hr8X65
lnPiE41M+G0Z7icEXiFyDBFDCtzx0x/RmaBokLathrFtI81UCx4gQPLaSVNMlvQA
539GsubSrO4LpHRNGg/weZ6EqQOXvHvkUkm2bDDJAoGATytFNxen6GtC0ZT3SRQM
WYfasdf3xbtuykmnluiofasd2sfmjnljkt7khghmghdasSDFGQfgaFoKfaawoYeH
C2XasVUsVviBn8kPSLSVBPX4JUfQmA6h8HsajeVahxN1U9e0nYJ0sYDQFUMTS2t8
RT57+WK/0ONwTWHdu+KnaJECgYEAid/ta8LQC3p82iNAZkpWlGDSD2yb/8rH8NQg
9tjEryFwrbMtfX9qn+8srx06B796U3OjifstjJQNmVI0qNlsJpQK8fPwVxRxbJS/
pMbNICrf3sUa4sZgDOFfkeuSlgACh4cVIozDXlR59Z8Y3CoiW0uObEgvMDIfenAj
98pl3ZkCgYEAj/UCSni0dwX4pnKNPm6LUgiS7QvIgM3H9piyt8aipQuzBi5LUKWw
DlQC4Zb73nHgdREtQYYXTu7p27Bl0Gizz1sW2eSgxFU8eTh+ucfVwOXKAXKU5SeI
+MbuBfUYQ4if2N/BXn47+/ecf3A4KgB37Le5SbLDddwCNxGlBzbpBa0=
-----END RSA PRIVATE KEY-----"""

private_key = paramiko.RSAKey(file_obj=StringIO(key_str))
transport = paramiko.Transport(('10.0.1.40', 22))
transport.connect(username='wupeiqi', pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()

transport.close()

print(result)

# 基于私钥字符进行连接
#
# 基于私钥字符进行连接





'''SFTPClient

用于连接远程服务器并执行上传下载

基于用户名密码上传下载：'''

import paramiko

transport = paramiko.Transport(('hostname',22))
transport.connect(username='wupeiqi',password='123')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()





import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', pkey=private_key )

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()




#!/usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko
import uuid

class SSHConnection(object):

    def __init__(self, host='172.16.103.191', port=22, username='wupeiqi',pwd='123'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def create_file(self):
        file_name = str(uuid.uuid4())
        with open(file_name,'w') as f:
            f.write('sb')
        return file_name

    def run(self):
        self.connect()
        self.upload('/home/wupeiqi/tttttttttttt.py')
        self.rename('/home/wupeiqi/tttttttttttt.py', '/home/wupeiqi/ooooooooo.py')
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport = transport

    def close(self):

        self.__transport.close()

    def upload(self,target_path):
        # 连接，上传
        file_name = self.create_file()

        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(file_name, target_path)

    def rename(self, old_path, new_path):

        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        cmd = "mv %s %s" % (old_path, new_path,)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果
        result = stdout.read()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        return result



ha = SSHConnection()
ha.run()



''''# 对于更多限制命令，需要在系统中设置
/etc/sudoers

 Defaults    requiretty
 Defaults:cmdb    !requiretty'''


import paramiko
import uuid

class SSHConnection(object):

    def __init__(self, host='192.168.11.61', port=22, username='alex',pwd='alex3714'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def run(self):
        self.connect()
        pass
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        return result

    def upload(self,local_path, target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path)

ssh = SSHConnection()
ssh.connect()
r1 = ssh.cmd('df')
ssh.upload('s2.py', "/home/alex/s7.py")
ssh.close()














import paramiko

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.6.7',port=22,username='teddy',password='11145')
stdin,stdout,stderr=ssh.exec_command('ls')
result=stdout.read()
ssh.close()





import paramiko
transport=paramiko.Transport('hostname',22)
transport.connect(username='wupipio',password='123')
ssh=paramiko.SSHClient()
ssh._transport=transport
stdin,stdout,stderr=ssh.exce_command('df')
print (stdout.read())

transport.close()







import paramiko
transport=paramiko.Transport('hostname',22)
transport.connect(username='wupeiqi',password='123456')
sftp=paramiko.SFTPClient.from_transport(transport)
sftp.put('/tmp/location.py','/tmp/test.py')
sftp.get('remove_path','local_path')
transport.close()















import paramiko
import  uuid

class SSHConnection(object):
      def __init__(self,host='172.16.103.191',port=22,username='teddy',pwd='123'):
          self.host=host
          self.port=port
          self.username=username
          self.pwd=pwd
          self.__k=None

      def create_file(self):
          file_name=str(uuid.uuid4())
          with open(file_name,'w') as f:
               f.write('sb')
          return file_name

      def run(self):
          self.connect()
          self.upload('/home/teddy/ttt.py')
          self.rename('/home/teddy/ttt.py','/home/tedddy/ooo.py')
          self.close()
      def connect(self):
          transport=paramiko.Transport((self.host,self.port))
          transport.connect(username=self.username,password=self.pwd)
          self._transport=transport


      def close(self):
          self.__transport.close()

      def upload(self,target_path):
          file_name=self.create_file()
          sftp=paramiko.SFTPClient.from_transport(self.__transport)
          sftp.put(file_name,target_path)


      def rename(self,old_path,new_path):
          ssh=paramiko.SSHClient()
          ssh._transport=self._transport
          cmd='mv %s %s'%(old_path,new_path)
          stdin,stdout,stderr=ssh.exec_command(cmd)
          result=stdout.read()

      def cmd(self,command):
          ssh=paramiko.SSHClient()
          ssh._transport=self._transport
          stdin,stdout,stderr=ssh.exec_command(command)
          result=stdout.read()


          return  result


ha=SSHConnection()
ha.run()

















































