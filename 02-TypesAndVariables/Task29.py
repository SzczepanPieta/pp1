import random

a=0
z=1

while a!=int(z):
    a=random.randint(1,6)
    z=input("Try to guess the number on the dice: ")
    print(f"Computer number on dice: {a}")
else:
    print(True)