#!/usr/bin/python
# -*- coding: utf-8 -*-
import dns.resolver

domain = raw_input('Please input an domin :')
MX = dns.resolver.query(domain, 'MX')
for i in MX:
    print 'MX preference = ', i.preference, 'mail exchange = ', i.exchange
