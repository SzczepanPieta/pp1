arr=[5,1,9,6,1]

max=arr[0]
min=arr[0]

for x in range(len(arr)):
    if arr[x]>max:
        max=arr[x]
    if arr[x]<min:
        min=arr[x]

print("Array:",arr)
diff=max-min
print("Result:",diff)

