#!/usr/bin/python
# -*- coding: utf-8 -*-
import paramiko
import os

hostname = '192.168.125.126'
username = 'root'

# 发送paramiko日志到syslogin.log文件
paramiko.util.log_to_file('syslogin.log')

# 创建一个SSHClient对象
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
privateKey = os.path.expanduser('~/.ssh/id_rsa')  #自定义私钥的存放路径
key = paramiko.RSAKey.from_private_key_file(privateKey) #创建私钥对象key

ssh.connect(hostname=hostname,username=username,pkey=key)
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()
