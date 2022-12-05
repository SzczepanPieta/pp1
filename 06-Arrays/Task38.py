arr=[1,23,5,382,1,17,4,906]

for x in range(len(arr)):
        print("-----",end="")

print("-")
for x in range(len(arr)):
    if arr[x]<10:
        print("|  ",arr[x],end="")
    if arr[x]<100 and arr[x]>10:
        print("| ",arr[x],end="")
    if arr[x]<1000 and arr[x]>100:
        print("|",arr[x],end="")
    

print("|")

for x in range(len(arr)):
        print("-----",end="")

print("-")
