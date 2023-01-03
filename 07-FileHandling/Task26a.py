file=open("07-FileHandling/thirdpower.txt","w")

for line in range(1,10):
    file.write(str(line))
    file.write(",")
    file.write(str(line**2))
    file.write(",")
    file.write(str(line**3))
    file.write("\n")

file.close()