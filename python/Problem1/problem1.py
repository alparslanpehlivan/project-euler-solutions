
x=3
i=1
y=0
temp=0

while x<1000:
    if x%3==0 or x%5==0:
        y+=x
        x+=1

        continue
    else:
        x+=1
        continue
print(y)
