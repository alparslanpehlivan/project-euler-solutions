# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:35:49 2019
"""

list_1=[]
sum=0

for line in open('dosya3.txt','r'):
    data = int(line)
    list_1.append(data)

#print(list_1)

for k in list_1:
   sum+=k

#print(sum)

sum=str(sum)

print(sum[0:10])

fname.close()