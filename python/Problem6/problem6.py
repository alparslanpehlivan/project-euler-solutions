# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:32:44 2019

"""

k=0
temp=0

for i in range(1,102):
    temp+=k
    k=(i**2)

print(temp)  

l=0
temp2=0
for i in range(1,102):
    temp2+=l
    l=i

print(temp2**2)  

print(temp2**2 - temp)