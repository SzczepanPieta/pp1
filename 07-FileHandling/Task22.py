f = open("copy.txt", "r")
copy = open("copylines.txt", "w")
for line in f:
    copy.write(line)
f.close()
copy.close()