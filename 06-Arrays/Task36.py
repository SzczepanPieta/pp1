arr=[2,5,8,1,3,7]

print("Segretated numbers: ",end="")
for x in range(len(arr)):
    if arr[x]%2==0:
        print(arr[x],end=" ")

for x in range(len(arr)):
    if arr[x]%2==1:
        print(arr[x],end=" ")