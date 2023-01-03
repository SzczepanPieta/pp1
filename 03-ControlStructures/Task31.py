a=1
b=1
z="*"
u=" "

if b<=2:
    for i in range(0,a):
        print(str(z)*b)

if b>2:
    for i in range(0,1):
        print(str(z)*b)

    for i in range(1,a-1): 
        print(z,str(u)*(b-4),z)

    for i in range(a-1,a):
        print(str(z)*b)
