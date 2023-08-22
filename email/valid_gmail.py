from re import *
f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\email\\data.txt","r")
valid_emails=set()
rule="[a-zA-Z0-9][a-zA-Z0-9_$#]*[@]gmail[.]com"
for id in f:
   id=id.rstrip("\n")
   matcher=fullmatch(rule,id)
   if matcher!=None:
      valid_emails.add(id)
print(valid_emails)