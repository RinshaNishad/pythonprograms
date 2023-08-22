#KL-08-bn-6785


from re import *
vehicle_no="KL-12-hg-9876"
rule="^[K][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}$"
matcher=fullmatch(rule,vehicle_no)
if matcher==None:
    print("invalid")
else:
    print("valid")