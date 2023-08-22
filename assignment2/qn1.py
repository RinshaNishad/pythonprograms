emplst=[]
for i in range(3):
    name=input("Enter three names:")
    emplst.append(name)
print(emplst)
# for j in range(3):
qn=input("Do u wantt to add another (yes/no):").strip().lower()
while qn=="yes":
    qn=input("Do u wantt to add another (yes/no):").strip().lower()
    if qn=="yes":
        name=input("Enter names:")
        emplst.append(name)
    else:
       break
print(f"Total no. of people invited to party is {len(emplst)}")