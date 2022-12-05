"""
arr1=[1,2,4]
arr2=[7,3,5,1,2,2,2]

i=0
j=0
m=len(arr1)

for i in range(len(arr2)):
    for j in range(len(arr1)):
        if arr1[j]==arr2[i]:
         print("it is a subset")
    if (j==m):
        print("it isn't a subset")

"""
def isSubset(arr1, arr2, m, n):
    i = 0
    j = 0
    z=0
    for i in range(n):
        for j in range(m):
            if(arr2[i] == arr1[j]):
                z=z+1
                break
 
        # If the above inner loop was
        # not broken at all then arr2[i]
        # is not present in arr1[]
        if (z == n):
            return 1
 
    # If we reach here then all
    # elements of arr2[] are present
    # in arr1[]
    return 0
 
 
# Driver code
if __name__ == "__main__":
 
    arr1 = [11, 1, 13, 21, 3, 22]
    arr2 = [11, 3, 7, 1]
 
    m = len(arr1)
    n = len(arr2)
 
    if(isSubset(arr1, arr2, m, n)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[]")
    