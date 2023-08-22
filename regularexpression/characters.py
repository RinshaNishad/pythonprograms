from re import *
# import re

text="AabaB$#bcdA976"
#[ab] either a or b
#[a-z] from a to z
#[a-zA-Z] all alphabets including caps
# matcher=finditer("[ab]",text)
# m1=finditer("[a-zA-Z]",text)
# m2=finditer("[a-zA-Z0-9]",text)
matcher=finditer("[^a-zA-Z0-9]",text)
# print(matcher)
# print(m1)
# print(m2)
print(matcher)

for m in matcher:
    print(m.group())     
    # print(m.start())     



#====================================
#[a-z]---/w
#[^a-z]---/W

#[0-9]---/d
#[^0-9]---/D

#space-/s
#a*---any no. of a
#a{2}---a repeat 2 time
#a{2,3}--a min-2 max-3