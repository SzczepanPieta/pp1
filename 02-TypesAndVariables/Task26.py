import math

a=int(input("triangle 1st side: "))
b=int(input("triangle 2nd side: "))
c=int(input("triangle 3rd side: "))

s=a+b+c/2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(area)


