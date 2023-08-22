#create an emptylst and access all elements from user
#add new elmnt to 2nd postn of lst which should be max of lst added by 10
emplst=[]

length=int(input("Enter size of list :"))
for i in range(length):
    num=int(input(f"Enter {i}th position element :"))
    emplst.append(num)
print(emplst)
maximum=max(emplst)
res=maximum+10
emplst.insert(2,res)
# print("Maximum value is :",maximum)
print(emplst)
