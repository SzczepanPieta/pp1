arr=[2,3,7,5,4]
print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(len(arr)-1)
print(len(arr)-2)
print(arr[0]+arr[len(arr)-1])
print(arr[len(arr)//2])

for i in arr:
    print(i, end=" ")

print()
  
i=0
while i<=len(arr)//2:
    print(arr[i], end=" ")
    i=i+1