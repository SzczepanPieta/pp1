import random

def rand_elem(array):
    index=random.randint(0,len(array)-1)
    return array[index]
    
for i in range(5):
    print(rand_elem([4,15,61,17,8]))