arr=["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]

max=arr[0]

for x in range(1,len(arr)):
    if len(max)<len(arr[x]):
        max=arr[x]

#print("Names: ","Genowefa","Onurfy","Celestyna","Alozjy","Pankracy")
print("Names: ",end="")
for x in range(len(arr)):
    print(arr[x],end=" ")    

print()

print("Longest name: ",max)
