arr=[5,4,3,2,6,5]

def string(ar):
    for x in range(len(ar)-1):
        print(ar[x],end="")
        print(",",end=" ")
    return ar[-1]
    

print("Array:",arr)
print("String:",end=" ")
n=string(arr)
print(n)

