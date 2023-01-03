x=input("File name: ")
file=open(x,"r")
ze=0
for line in file:
    ze=ze+1
print("Numbers of lines: ",ze)
file.close()



