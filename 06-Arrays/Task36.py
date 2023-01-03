def odd(s):
    for x in range(len(s)):
        if s[x]%2==0:
            print(s[x],end=" ")
    for i in range(len(s)):
        if s[i]%2==1:
            print(s[i],end=" ")

print("Segretated numbers: ",end="")
arr=[2,5,8,1,3,7]
odd(arr)

print()

def odda(a):
    z=[]
    for x in range(len(a)):
        if a[x]%2==0:
            z.append(a[x])
    for i in range(len(a)):
        if a[i]%2==1:
            z.append(a[i])
    return z

print("Segretated numbers: ",end="")
print(odda(arr))

              