#starting with an alphabet
#special characters $ and _
#length limit 1-10
from re import *
rule="[a-zA-Z][a-zA-Z0-9_$]{0,10}"
var_name="num_one"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")