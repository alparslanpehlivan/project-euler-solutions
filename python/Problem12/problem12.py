# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:35:49 2019

@author: PEHLIVA
"""

factors=0
h=1
num=1
k=2

while factors<500:
    
   
    h+=k
    k+=1
    
    for i in range(1,h):     
        
        
        
        if h%i==0:
                
            factors+=1

    if factors==500:

        break
                
    factors=0
                
              
    
print(h)
print(factors)

        