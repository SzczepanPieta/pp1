file=open("07-FileHandling/countries.txt","r")
for line in file:
    print(line, end="")
file.close()