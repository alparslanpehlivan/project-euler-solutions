n1=0
n2=1
temp=0
sum=0
while n2<4000000:
    temp=n2
    n2=n2+n1
    n1=temp
    if n2%2==0:
        sum+=n2
    continue
print(sum)