file=open("07-FileHandling/numbers.txt","r")
sum=0
for line in file:
    print(int(line))
    sum=int(line)+sum
file.close()
print(sum)