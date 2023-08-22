from re import *
fread=open("C:\\Users\\DELL\\Desktop\\pythonworks\\exam.py\\setA\\validate_pannumber\\data.txt","r")
fwrite=open("C:\\Users\\DELL\\Desktop\\pythonworks\\exam.py\\setA\\validate_pannumber\\validpannumb.txt","w")

rule="^[A-Z]{5}[0-9]{4}[A-Z]{1}?"

for pan in fread:
    pan=pan.rstrip("\n")
    matcher=fullmatch(rule,pan)
    if matcher!=None:
        fwrite.write(str(pan)+"\n")
         
    