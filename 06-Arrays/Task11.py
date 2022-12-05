arr=[-15,8,-31,47,-2,19]

min=arr[0]
max=arr[0]
   

for x in range(1,len(arr)):
    if min>arr[x]:
        min=arr[x]
    if max<arr[x]:
        max=arr[x]

print(min)
print(max)    
