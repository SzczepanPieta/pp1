arr1=[1,0,4,9,6]
arr2=[6,8,3,1,0,5,7]

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return

bubbleSort(arr1)
bubbleSort(arr2)

def median(array):
    for x in range(len(array)):
        med=array[len(array)//2]
        return med

m=median(arr1)
s=median(arr2)


print("Sorted array is:",end=" ")
for i in range(len(arr1)):
    print(arr1[i], end=" ")

print()

print("Mediana is:",m)

print("Sorted array is:",end=" ")
for i in range(len(arr2)):
    print(arr2[i], end=" ")

print()
print("Mediana is:",s)



