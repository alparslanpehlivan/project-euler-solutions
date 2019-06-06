# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 19:14:26 2019

@author: PEHLIVA
"""


num2=0
num=2
toplam=[]
#toplam.append(8)
#print('Value: ',toplam)

for k in range(2,2000000):
    
    for i in range(2,k):
        
        if k%i == 0:
            
            break
            
    else:
        
        print(k)
        toplam.append(k)

#print('Value: ',toplam)
print('Sum: ',sum(toplam))