arr=[4,2,8,4,7,9,5]

def minmax(array):
    min=array[0]
    max=array[0]
    for x in range(len(array)):
        if min>arr[x]:
            min=arr[x]
        if max<arr[x]:
            max=arr[x]
    sam=[min,max]
    return sam
    

n=minmax([4,2,8,4,7,9,5])
print("Array: ",arr)
print("Result: ",n)

