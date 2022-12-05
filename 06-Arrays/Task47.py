import random

arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j]=random.randint(1,9)

print("Before changes: ",arr)

l=arr[2][-1]
s=arr[0][-1]

for i in range (len(arr)):
        arr[0][-1]=l
        arr[2][-1]=s

print("After Changes: ",arr)