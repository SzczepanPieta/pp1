file=open("07-FileHandling/numbers24.txt","w")
for line in range(1,51):
    file.write(str(line))
    file.write("\n")
file.close()
