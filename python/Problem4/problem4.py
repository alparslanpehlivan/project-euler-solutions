# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:09:08 2019

@author: PEHLIVA
"""


a=100
b=100
d2=0

for a in range(100,1000):
    for b in range(100,1000):
        c=a*b
        d=str(c)
        if d == d[::-1]:
            if int(d)>int(d2):
                d2=d
                print(a,b,d2)
            #print(d2)
            continue
        else:
            continue
print(d2)