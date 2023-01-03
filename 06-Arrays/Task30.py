arr=[15,38,7,23,14]

def occurs(number,array):
    for i in range(len(array)):
        if number==array[i]:
            return True

print(occurs(14,arr))

xed=int(input("Number: "))

print("Array: ",end="")

for i in range(len(arr)):
    print(arr[i],end=" ")

print()

a=occurs(xed,arr)

if a==True:
    print(f"Result: number {xed} appers in the array")


    

