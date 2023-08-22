#import packageName
import re
sen="ammu is a very good student in may batch"
sen2="ammu is a very good student in may batch  "
x=re.search("^ammu",sen)
y=re.search("^Ammu",sen)
z=re.search("very",sen)
en=re.search("batch$",sen)
st_en=re.search("^ammu.*batch$",sen)
st_en2=re.search("^ammu.*batch$",sen2)
st_en3=re.search("^ammu.*  $",sen2)
# print(x)
# print(y)
# print(z)
# print(en)
print(st_en)
print(st_en2)
print(st_en3)


#==> ^ symbol-used to fnd whthr the sntnc is strt with that charctr
#==> (^--caret symbol)
