x=0
y=1

print(x,y,end=" ")

for i in range(48):
    sum=x+y
    print(sum,end=" ")

    x=y
    y=sum
