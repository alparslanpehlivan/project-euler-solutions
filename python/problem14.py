# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:44:55 2019

@author: PEHLIVA
"""

temp=0

chain=0

k=0

for i in range(2,1000000):
    
    #if i%1000==0:
        
        #print(i)
    
    k=i
    
    while k!=1:
        
        chain+=1
        
    
        while k>1 and k%2==0:
            
            k=k/2
            
        while k>1 and k%2!=0:
            
            k=3*k+1
            
        if temp<chain:
            
            temp=chain
            
            print(i)
            
        if k==1:
            
            chain=0

    