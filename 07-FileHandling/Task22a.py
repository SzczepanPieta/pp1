file=open("07-FileHandling/copy.txt","w")
f=open("07-FileHandling/copylines.txt","r")
for line in f:
    file.write(line)
file.close()
f.close()