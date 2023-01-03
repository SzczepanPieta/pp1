import random

def read_number():
    x=input("Write a number: ")
    return int(x)

def generate_number():
    y=random.randint(1,9)
    return int(y)