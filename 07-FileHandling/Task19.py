stop=1
with open("random.txt") as f:
    for line in f:
        print(line, end="")
        stop+=1
        if stop==5:
            input("Press Enter to continue...")

f.close()






    

    