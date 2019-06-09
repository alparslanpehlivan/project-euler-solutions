# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:40:43 2019
"""

temp=1

n1=1
n2=1
n3=2
chain=0
temp1=1
total=0
k=0

while k < 1001:
    
    n1=temp1
    n2=temp
    total=n2+n1
    temp=total
    temp1=n2
    k=len(str(total))
    
    chain+=1
    
    if k==1000:
        
        print(chain+2)

#f=str(total)
#f
print(chain+2)