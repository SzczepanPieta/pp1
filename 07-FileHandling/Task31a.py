import re

file=open("07-FileHandling/file31.txt","r")
reader=file.read()
print(reader)

letter=re.findall("\w{6,}",reader)
print(letter)
for line in letter:
    print(line)
