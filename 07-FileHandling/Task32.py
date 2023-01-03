import re

file=open("07-FileHandling/grades.txt","r")
reader=file.read()


grade=re.findall("\d.{1,2}",reader)
print(grade)
z=0
for line in grade:
    z=z+float(line)
arth=z/len(grade)
print(arth)