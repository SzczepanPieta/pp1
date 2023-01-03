with open("07-FileHandling/extfile.txt","w") as f:
    for line in range(1,51):
        f.write(str(line))
        f.write("\n")
        
        

f.close()

