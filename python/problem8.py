# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:42:37 2019

@author: PEHLIVA
"""

fname=open('dosya2.txt','r')
fname2=open('dosya3.txt','w')
oku=fname.read()
oku3=oku.replace('\n','')
#print(oku)
oku2=fname2.write(oku3)
print(oku2)


k=0
temp=0

for i in range(13,1000):
    #oku3[i:]
    #print(oku3[i:i+1])
    k = int(oku3[i])*int(oku3[i-1])*int(oku3[i-2])*int(oku3[i-3])*int(oku3[i-4])*int(oku3[i-5])*int(oku3[i-6])*int(oku3[i-7])*int(oku3[i-8])*int(oku3[i-9])*int(oku3[i-10])*int(oku3[i-11])*int(oku3[i-12])
    print(temp)
    print(k)
    
    if k>temp:
        temp=k

print(temp)

fname2.close()
fname.close()