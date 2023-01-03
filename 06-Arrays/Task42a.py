def prin(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j],end=" ")
        print()

def sumk(array,k):
    sum=0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if j ==k:
                sum=sum+array[i][j]
    return sum

def sumka(array,k):
    sum=0
    for i in range(len(array)):
        sum=sum+array[i][k]
    return sum

arr=[[3,4,5,6],[3,4,2,0]]

sum=0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if j==len(arr[0])-1:
           sum=sum+arr[i][j]

        

prin(arr)
print(sum)
print(sumk(arr,2))
print(sumka(arr,2))
 