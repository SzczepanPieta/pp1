import random

file=open("07-FileHandling/numbers25.txt","w")
for line in range(50):
    file.write(str(random.randint(100,999)))
    file.write("\n")
file.close