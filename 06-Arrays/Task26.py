def compare(array1, array2):
        if len(array1)!=len(array2):
            return False
        else:
            for x in range(len(array1)):
                if array1[x]!=array2[x]:
                    return False
            return True

arr1=["water","book","sky"]
arr2=["water","book","sky"]

print("Array1:",arr1)
print("Array2:",arr1)

if compare(arr1, arr2)==False:
    print("Comparasion: arrays are not the same")
else:
    print("Comparasion: arrays are the same")