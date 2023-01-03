arr1=[2,5,7,3,5]
arr2=[5,7]

def check(array1, array2):
    for i in range(len(array2)):
        if array2[i] not in array1:
            return False
    return True

print(check(arr1, arr2))