# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:57:17 2019

@author: PEHLIVA
"""
 
"""
import numpy as np
data = np.loadtxt("file.txt", delimiter=" ")
"""

fname=open('dosya.txt','r')
fname2=open('dosya5.txt','w')
#oku=fname.read()

#print(oku)
k=[]
k_int=[]
temp=0
temp2=0
temp3=0
temp4=0
temp5=0
h,o=0,0

for line in open('dosya.txt','r'):
    data = line.split()
    k.append(data)

#$print(k)

for i in range(0,17):
    for j in range(0,20):
        UST = int(k[i][j])*int(k[i+1][j])*int(k[i+2][j])*int(k[i+3][j])
        if temp<UST:
            temp=UST
print(temp)

for i in range(0,20):
    for j in range(0,17):
        YAN = int(k[i][j])*int(k[i][j+1])*int(k[i][j+2])*int(k[i][j+3])
        if temp2<YAN:
            temp2=YAN
print(temp2)

for i in range(0,17):
    for j in range(0,17):
        DIA = int(k[i][j])*int(k[i+1][j+1])*int(k[i+2][j+2])*int(k[i+3][j+3])
        if temp3<DIA:
            temp3=DIA
print(temp3)

for i in range(0,20):
    for j in range(0,17):
        DIA2 = int(k[i][j])*int(k[i-1][j+1])*int(k[i-2][j+2])*int(k[i-3][j+3])
        if temp4<DIA2:
            h,o=i,j
            temp4=DIA2
print(h,o)
print(temp4)

fname.close()
fname2.close()

#res = list(map(int, k))
#print(res)
#for i in range(len(k)):
#    k[i]=int(k_int[i])


#for i in range(len(k)):
#    k[i] = int(k[i])

#print(k_int)


#y = ''.join(k) # converting list into string
#z = int(y)
#print(z)

#y = ''.join(map(str, k))
#z = int(y)

