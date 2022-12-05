arr=[3,6,9,1,4]

i=int(input("Write a number, and we will write all the numbers of the elements that are greater than your number: "))

print("The quantity of number is: ",end="")
a=0
for x in range(len(arr)):
    if arr[x]>i:
        a=a+1
print(a)      


