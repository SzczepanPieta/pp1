arr=[4,2,8,4,7,9,5]

def minmax(array):
    min=array[0]
    max=array[0]
    for i in range(len(array)):
        if array[i]<min:
            min=array[i]
        if array[i]>max:
            max=array[i]
    sam=[min,max]
    return sam



print("Array:",arr)
print("Results:",minmax(arr))