arr=[2,3,2,5,8,1,9,8]
ile=[0,0,0,0,0,0,0,0]

print("Array: ",end="")

for x in range(len(arr)):
    print(arr[x],end=" ")

print()
print("Unique elements: ",end=" ")

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            ile[i]=ile[i]+1

for c in range(len(ile)):
    if ile[c]==1:
        print(arr[c],end=" ")







#for i in range(len(arr)):



     
