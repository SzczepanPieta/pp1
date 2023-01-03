arr=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

i=0
x=0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j],end=" ")
    print()

even=0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]%2==0:
            even=arr[i][j]+even

print(even) 
            



