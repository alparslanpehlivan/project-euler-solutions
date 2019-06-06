# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


k=0
n2=0



for num in range(2,50):
    while k<10001:
        for i in range (2,num):
            if num%i == 0:
                #print('i: ',i)
                #print('num: ',num)
                break
        else:
                n2=num
                k+=1
                print('{}. eleman: {} '.format(k,n2))
        num+=1
      
#print('n2: ',n2)  



































