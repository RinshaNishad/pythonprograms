from re import *
password=input("enter your password :")
rule="[a-zA-Z0-9_$#@%&*!]{6,16}"
matcher=fullmatch(rule,password)
if matcher:
    print("it is valid...")
else:
    print("not valid...")