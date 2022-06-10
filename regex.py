#!/bin/python3

import re

file = 'vhost2.conf'

f=open(file, 'r')
text = f.read()
f.close()

p = re.compile('<VirtualHost.*>(.+)</VirtualHost>', re.I|re.M|re.S) 

res = p.findall(text)

print(res)
