def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
 
 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
arr1 = [3,7,0,-12,34,2,5]
arr2 = [1,-2,30,-17,3,22,15]
 
bubbleSort(arr)
bubbleSort(arr1)
bubbleSort(arr2)
 
 
 
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

print()

print("Sorted array is:")
for i in range(len(arr1)):
    print("% d" % arr1[i], end=" ")

print()

print("Sorted array is:")
for i in range(len(arr2)):
    print("% d" % arr2[i], end=" ")