x=input("Enter the dog's age in human years: ")
y=int(x)
z=0

if y<=2 and y>0:
    z=10.5*y
if y>2:
    z=(10.5*2)+((y-2)*4)

print(f"The dog's age in dog's years is {z} years")
