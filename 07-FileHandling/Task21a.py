file=open("07-FileHandling/copy.txt","w")
f=open("07-FileHandling/copylines.txt","r")
file_content=f.read()
file.write(file_content)
f.close()
file.close()
