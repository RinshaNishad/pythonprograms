import re
# text="ababababa"
# text1="bbaaaabbbbbcc"
# t=re.search("[a]{4}",text)
# t1=re.search("[a]{4}",text1)
# print(t)
# print(t1)

#======================================================================

# text="abcd1234"
# t1=re.search("[a-z]{4}",text)
# print(t1)

#======================================================================

stri="abDARG5643"
s=re.search("[a-z]{2}[A-Z]{4}",stri)
print(s)