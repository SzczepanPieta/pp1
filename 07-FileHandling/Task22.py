f = open("c07-FileHandling/opy.txt", "r")
copy = open("07-FileHandling/copylines.txt", "w")
for line in f:
    copy.write(line)
f.close()
copy.close()