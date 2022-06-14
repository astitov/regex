#!/bin/python3

import re

file = 'vhost2.conf'

#with open(file, 'r') as f:
#  for line in f:
#    text += line.strip()

f = open(file, 'r')
text = f.read()
f.close

p = re.compile('<VirtualHost[^>]*?>(.+?)</VirtualHost>', re.I | re.S) 
res = p.findall(text)


print(text)
print(res)
