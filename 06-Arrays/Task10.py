arr=[1,2,3,4,5]

arr[0]=arr[0]-1
#arr[0]-=1
print(arr)

arr[-1]=arr[-1]+4
#arr[-1]+=4
print(arr)

#arr[len(arr)//2]=arr[len(arr)//2]*2
arr[len(arr)//2]*=2
print(arr)

for x in range(len(arr)):
    #arr[x]=arr[x]+3
    arr[x]+=3
print(arr)