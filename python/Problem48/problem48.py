x,y,a,k, l=1,1,0, [], []
while x<1001:
    a+=x**y; x+=1; y+=1
print(int(str(a)[-10:]))