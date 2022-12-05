arr=[12,6,4,9,10]

def star(n):
    print(n,": ",end="")
    for x in range(n-1):
         print("*",end="")
    return "*"

for x in range(len(arr)):
    print(star(arr[x]))




def star2(n):
    napis=""
    for x in range(n):
        napis=napis + '*'
    return napis

for i in arr:
    print(i,":", star2(i))
