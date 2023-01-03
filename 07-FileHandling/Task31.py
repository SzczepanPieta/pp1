import re

y = 'to be or not to be'
x = y[0b11:0xB]

words=re.findall(x,y)
print(words)


z="1.22.333.4444.55555.666666"

echo=re.match("\d+",z)
print(echo)
