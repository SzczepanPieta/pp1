def great(array,f):
    z=0
    for x in range(len(array)):
        if array[x]>f:
            z+=1
            
    return z

arr=[3,6,9,1,4]

fd=int(input("Put a number here: "))
print(great(arr,fd))
aq = [1,2,3,4,6,7,-2]
fq=int(input("Put a second number here: "))

print(great(aq,fq))


