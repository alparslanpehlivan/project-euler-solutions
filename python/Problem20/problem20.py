# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:29:18 2019
"""


sum=1
k=0

for i in range(1,101):
    
    sum*=i

sum=str(sum)

for i in range(0,len(sum)):
  
    k+=int(sum[i])
    
print(k)