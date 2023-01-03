arr1=[1,0,4,9,6]
arr2=[6,8,3,1,0,5,7,13,7,8,9,3]




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

print(arr1)
print(arr2)

def median(arr1):
    arr = arr1.copy()
    bubbleSort(arr)
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2] + arr[n // 2 - 1]) / 2
    else:
        return arr[n // 2]

print("median: ",median(arr1))
print("median: ",median(arr2))




