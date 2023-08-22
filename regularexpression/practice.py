import re
sent="hi hello hi hi hello good 13, afternoon hi hello hide inhile 11:38,78"
ct=sent.count("hi")
print(ct)
ct1=re.findall("hi",sent)
print(ct1)
nums=re.findall("[0-5][0-9]",sent)
print(nums)
ct2=re.findall("ll",sent)
print(ct2)
#===================================================================

import re
resi=input("enter a residence number :")
ekm=re.search("^0484",resi)
tvm=re.search("^0471",resi)
ijk=re.search("^0480",resi)
tcr=re.search("^0487",resi)
mpr=re.search("0494",resi)
ksd=re.search("^04994",resi)
cct=re.search("0495",resi)
if ekm:
    print("ekm")
elif tvm:
    print("tvm")
elif ijk:
    print("ijk")
elif tcr:
    print("tcr")
elif mpr:
    print("mpr")
elif ksd:
    print("ksd")
else:
    print("cct")

#===============================or=====================================
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



