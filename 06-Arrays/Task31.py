arr=[5,1,9,6,1]



def findmax(array):
    max=0
    for x in range(len(array)):
        if max<=array[x]:
            max=array[x]
    return max



def findkmax(array,k):
    temp = array.copy()
    if k>len(temp):
        k=len(temp)
    b=findmax(temp)
    for x in range(k-1):
        temp.remove(b)
        b=findmax(temp)
    return b

        
   




print(arr)
print(findkmax(arr,2))
print(arr)
print(findkmax(arr,20))