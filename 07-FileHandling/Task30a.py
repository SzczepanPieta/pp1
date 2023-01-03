import re

message="To be, or not to be, that is the question"

spaces=re.findall("\s",message)

print(len(spaces)+1)