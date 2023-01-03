file=open("07-FileHandling/copylines.txt","r")
k=0
for line in file:
    print(line,end="")
    k+=1
    if (k)%5==0:
        input("Do you want to continue")
file.close()
