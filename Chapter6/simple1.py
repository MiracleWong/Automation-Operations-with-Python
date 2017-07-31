#!/usr/bin/python
# -*- coding: utf-8 -*-
import paramiko

hostname = '192.168.24.83'
#hostname = '192.168.125.126'
username = 'root'
password = '123456'

# 发送paramiko日志到syslogin.log文件
paramiko.util.log_to_file('syslogin.log')

# 创建一个SSHClient对象
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()

ssh.connect(hostname=hostname,username=username,password=password)
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()
