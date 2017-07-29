#!/usr/bin/python
# -*- coding: utf-8 -*-
import paramiko
import sys
reload(sys) 
sys.setdefaultencoding("utf-8")

hostname = '192.168.125.126'
username = 'root'
password = '123456'
port=22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put("hello.txt", "/root/hello.txt") #上传文件
    sftp.get("/root/hello.txt", "hello1.txt") #下载文件
    sftp.mkdir("/root/userdir",0755) #创建目录
    print "Create successgfully"
    sftp.rmdir("/root/userdir") # 删除目录
    sftp.rename("/root/testfile.sh","/root/test.sh") # 文件重命名
    print sftp.stat("/root/test.sh") # 打印文件信息
    print sftp.listdir("/root") # 打印目录列表
    t.close()
except Exception, e:
    print str(e)
