#!/usr/bin/python
# -*- coding: utf-8 -*-
from IPy import IP

ip_s = raw_input('Please input an IP or non-range: ')
ips = IP(ip_s)
if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())
    print('reverse address: %s' % ips.reverseNames()[0])
    print('subnet: %s' % len(ips))
else:
    print('reverse address: %s' % ips.reverseNames()[0])

print('hexadecimal %s' % ips.strHex())
print('binary %s' % ips.strBin())
print('iptype %s' % ips.iptype())
