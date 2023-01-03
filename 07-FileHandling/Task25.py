import random

with open("07-FileHandling/afile.txt","w") as f:
    for i in range(50):
        f.write(str(random.randint(100,999)))
        f.write("\n")

f.close()


