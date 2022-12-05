arr=[15,8,31,47,2,19]

print("existed array:",end=" ")
i=0
while i<len(arr):
    print(arr[i],end=" ")
    i=i+1

print()

print("reverse array:",end=" ")

x=(len(arr)-1)
while x>=0:
    print(arr[x],end=" ")
    x=x-1