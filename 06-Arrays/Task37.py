arr=[5,4,3,2,6,5,2,3]



def test2(ar):
    res=""
    for x in range(len(ar)-1):
        res = res+str(ar[x])+", "
    res=res+str(ar[len(ar)-1])
    return res



        

print("Array:",arr)
print("String:",end=" ")

print(test2(arr))
print(arr)
