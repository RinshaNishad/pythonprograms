#mobile number verification
#(check whether a mobile number is 10 digit flwd by +91(a prpr mobno.))
from re import *
mob=input("enter your mobile number with country code :")
check=match("[+]91[0-9]{10}$",mob)
if check==None:
    print("given number is invalid")
else:
    print("given number is valid")
