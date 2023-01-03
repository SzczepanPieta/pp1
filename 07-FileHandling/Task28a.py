import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
z=0
for i in range(len(temperatures)):
    z=z+int(temperatures[i])
srednia=z/len(temperatures)
print(srednia)
