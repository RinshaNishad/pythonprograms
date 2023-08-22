# lst=[2,3,4,5]
# lst.insert(1,6)  #lstname.insert(position,value)
# lst.insert(0,1)
# print(lst)

#creatng empty list
emplst=[]
print(emplst)
length=int(input("Enter size of list :"))
for i in range(length):
    num=int(input(f"Enter {i}th position element :"))
    emplst.append(num)
print(emplst)
