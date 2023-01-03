import re

message = "Tuesday: 22C, Wednesday: 21C, Thuorsday: 26C "
temperatures = re.findall("\d{2}",message)
z=0
for i in range(len(temperatures)):
    z=z+int(temperatures[i])
srednia=z/len(temperatures)
print(srednia)


ile_c=re.findall("[C]",message)
print(len(ile_c))
ile_da=re.findall("da",message)
print(ile_da)
print(len(ile_da))

print(re.findall("\\\\",message))

