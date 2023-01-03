arr=[5,1,9,6,1]

def min(array):
    k=array[0]
    for x in range(len(array)):
        if array[x]<k:
            k=array[x]
    return k


print(min(arr))

def max(array):
    m=array[0]
    for i in range(len(array)):
        if array[i]>m:
            m=array[i]
    return m

print(max(arr))

def extraction(array):
    z=max(array)
    s=min(array)

    ext=z-s
    return ext

print(extraction(arr))

