from re import *

text="luminar techno lab luminar techno hub"
matcher=finditer("luminar",text)

count=0
for m in matcher:
    print(m.group())     #----to check whether it is present
    print(m.start())     #----to check the position
    count+=1
print(count)

# ct=text.count("luminar")
# print(ct)