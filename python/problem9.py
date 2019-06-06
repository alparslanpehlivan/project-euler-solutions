# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 19:03:03 2019

@author: PEHLIVA
"""

a=1
b=1
c=1

for a in range(1,600):
    for b in range(1,600):
        for c in range(1,600):
            if c**2==a**2+b**2:
                if a+b+c==1000:
                    print(a,b,c)
                    break
                else:
                    continue
            else:
                continue
print(a,b,c)