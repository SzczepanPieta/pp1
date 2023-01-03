arr=[2,3,4,5,6,7,8,9,2,2]

x=int(input("Enter a number: "))
z=0

for i in range(len(arr)):
    if x==arr[i]:
       z=z+1
print("This numbers occures this many times in this array: ",z)       