arr=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if [i]==[j]:
            arr[i][j]=1
        print(arr[i][j],end=" ")
    print()