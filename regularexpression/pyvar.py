#fst character starts with an alphabet or underscore
#second character any number of alphabets and digits



from re import *
rule="[a-zA-Z_][a-zA-Z0-9_]*"
var_name=input("enter a variable name :")
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")
