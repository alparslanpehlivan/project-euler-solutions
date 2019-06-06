# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:51:08 2019
"""

from num2words import num2words

sum=0

for i in range(1,1001):
    print(num2words(i))
    #num2words(k)=num2words(i).replace(' ','').replace('-','')
    sum+=len(num2words(i).replace(' ','').replace('-',''))

print(sum)