#a*---any no. of a
#a{2}---a repeat 2 time
#a{2,3}--a min-2 max-3
#===========================================

#fst character starts k-m
#scnd character should be a digit that must be divisible by 3
#any number of characters

from re import *
var_name=input("enter a variable name :")
rule="[k-m][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,var_name)
if matcher!=None:
    print("valid")
else:
    print("invalid")
