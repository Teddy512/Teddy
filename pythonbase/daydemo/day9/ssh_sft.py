__author__ = "Alex Li"

import paramiko
transport = paramiko.Transport(('10.0.0.31', 52113))
transport.connect(username='root', password='123456')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('笔记', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/root/oldgirl.txt', 'fromlinux.txt')

transport.close()



# 传文件命令
'scp -r -P 22 /srv/odoox/hengyi rejen@192.168.6.7:/home/rejen/'

# 复制命令
'cp -r /home/rejen/hengyi /opt/odoo/'

# 远程连接
'ssh ks@192.168.1.152'

