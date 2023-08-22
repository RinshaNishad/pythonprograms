
from re import *
vehicle_no="TV-12-kh-7896"
rule="^[A-Z]{2}[-][0-9]{2}[-][a-z]{2}[-][0-9]{4}$"
matcher=fullmatch(rule,vehicle_no)
if matcher==None:
    print("invalid")
else:
    print("valid")