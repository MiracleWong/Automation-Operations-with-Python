#!/usr/bin/python
# -*- coding: utf-8 -*-
import paramiko

hostname = '192.168.125.126'
username = 'root'
password = '123456'
port=22

try:
    
except Exception, e:
    print str(e)
# 创建一个SSHClient对象
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
privateKey = os.path.expanduser('~/.ssh/id_rsa')  #自定义私钥的存放路径
key = paramiko.RSAKey.from_private_key_file(privateKey) #创建私钥对象key

ssh.connect(hostname=hostname,username=username,pkey=key)
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()
