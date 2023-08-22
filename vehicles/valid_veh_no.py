from re import *
f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\vehicles\\data.txt","r")
kerala_veh=set()
tml_veh=set()
ker_rule="^[K][L][-][0-9]{2}[-][a-zA-Z]{1,2}[-][0-9]{4}$"
tn_rule="^[T][N][-][0-9]{2}[-][a-zA-Z]{1,2}[-][0-9]{4}$"

for v in f:
    v=v.rstrip("\n")
    matcher1=fullmatch(ker_rule,v)
    matcher2=fullmatch(tn_rule,v)

    # print(v)
    if matcher1!=None:
      kerala_veh.add(v)
    elif matcher2!=None:
      tml_veh.add(v)

print(kerala_veh,":valid kerala vehicle numbers")
print(tml_veh,":valid tamilnadu vehicle numbers")

