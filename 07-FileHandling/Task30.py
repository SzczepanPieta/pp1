import re

question="To be, or not to be, that is the question"
words=re.findall("[a-zA-Z]",question)
find=re.findall("\s",question)
print(words)
s=1
s=s+int(len(find))

print(s)