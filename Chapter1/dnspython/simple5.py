#!/usr/bin/python
# -*- coding: utf-8 -*-
import dns.resolver
import os
import httplib

iplist = []  # 定义域名IP列表变量
#appdomain = "www.google.com.hk"
appdomain = "www.baidu.com"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print "dns resolver error: " + str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    print iplist
    print iplist[0] + ":" + iplist[1]
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET","/",headers={"HOST":appdomain})
        r=conn.getresponse()
        getcontent = r.read(15)
    finally:
        if getcontent=="<!doctype html>":
            print ip + "  OK"
        else:
            print ip + "   Error"

def main():
    if get_iplist(appdomain) and len(iplist)>0:
        pass
        #for ip in iplist:
        #    checkip(ip)
    else:
        print "dns resolver error"

if __name__ == '__main__':
    main()
