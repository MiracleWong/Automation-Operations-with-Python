#!/usr/bin/python
# -*- coding: utf-8 -*-
import dns.resolver

domain = raw_input('Please input an domin :')
NS = dns.resolver.query(domain, 'NS')
for i in NS.response.answer:
    for j in i.items:
        print j.to_next()
