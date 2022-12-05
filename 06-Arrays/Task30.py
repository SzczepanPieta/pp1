arr=[15,38,7,23,14]

def occurs(number,array):
    for x in range(len(array)):
        if number==array[x]:
            return True

ax=occurs(12,[12,3,4])
print(ax)

x=int(input("Number: "))
print("Array :",end="")
for j in range(len(arr)):
    print(arr[j],end=" ")

print()

for i in range(len(arr)):
    if x==arr[i]:
        print("number",x,"appers in the array")
    

