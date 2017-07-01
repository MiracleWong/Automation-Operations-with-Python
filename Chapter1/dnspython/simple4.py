#!/usr/bin/python
# -*- coding: utf-8 -*-
import dns.resolver

domain = raw_input('Please input an domin :')
CNAME = dns.resolver.query(domain, 'CNAME')
for i in CNAME.response.answer:
    for j in i.items:
        print j.to_next()
