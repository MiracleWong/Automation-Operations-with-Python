#!/usr/bin/python
# -*- coding: utf-8 -*-
import dns.resolver

domain = raw_input('Please input an domin :')
A = dns.resolver.query(domain, 'A')
#print A.response.answer
#print A.response.answer[1].items
iplist = []
for i in A.response.answer:
    for j in i.items:
        iplist.append(j.address)
    print iplist[0] + "-----" + iplist[1]
