arr=[2,3,2,5,8,1,9,8]

print("Array: ",end="")

for i in range(len(arr)):
    print(arr[i],end=" ")

print()    

print("Unique elements: ",end="")

for j in range(len(arr)):
    z=0
    for f in range(len(arr)):
        if arr[j]==arr[f]:
            z=z+1
    if z==1:
        print(arr[j],end=" ")
            









            












     
