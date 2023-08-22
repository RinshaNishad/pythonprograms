# import re
# mob=input("enter your mobile number with country code :")
# check=re.search("^91 ",mob)
# if check:
#     print("given number is indian")
# else:
#     print("given number is foriegn")

#===============================or==================================

# import re
from re import *
mob=input("enter your mobile number with country code :")
# check=re,search("[+]91",mob)
check=search("^[+]91",mob)
if check:
    print("given number is indian")
else:
    print("given number is foriegn")
