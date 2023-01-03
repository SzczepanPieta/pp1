with open("07-FileHandling/filename.txt","r") as f:
    for line in f:
        print(line, end="")    

f.close()