#!/usr/local/bin/python
from fabric.api import *

env.user = 'root'
env.hosts = ['192.168.125.116','192.168.125.118']
env.password = '123456'

@runs_once
def local_task():
    local("uname -a")

def remote_task():
    with cd("/data/logs"):
        run("ls -l")