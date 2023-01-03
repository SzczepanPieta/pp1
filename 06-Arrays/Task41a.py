
def wys(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print()

arr=[[2,3,4,5],[1,2,0,9]]
print(arr)

wys(arr)


wys([[2,3],[1]])