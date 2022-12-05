arr=[1,3,4,6,7]

odd=0
even=0
x=0

while x<(len(arr)):
    if arr[x]%2==0:
            even=even+1
    else:
            odd=odd+1
    x=x+1

print("Number of odd numbers:",odd)
print("Number of even numbers:",even)
