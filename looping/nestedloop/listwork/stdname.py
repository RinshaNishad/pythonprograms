#create a list of studnt name
#check for a particular name in the list given by user
#if name is present then change the name to "anamika" if that particlr
#name is not present add "amal" to 1st postn.
# stud_name=[]


# length=int(input("Enter size of list :"))
# for i in range(length):
#     name=input(f"Enter name in {i}th position :")
#     stud_name.append(name)
# ch_name=input("Enter name to check :")
# for s in range(length):
#     if stud_name[s]==ch_name:
#         stud_name[s]="Anamika"
      
#         break
#     elif s==length-1:
#         stud_name.insert(1,"Amal")
# print(stud_name)

#Assgn:If duplicates values are present how the values will be changed
#if a match found or not


stud_name=[]
flag=0  #this can be any variable name eg:rep,non,dem

length=int(input("Enter size of list :"))
for i in range(length):
    name=input(f"Enter name in {i}th position :")
    stud_name.append(name)
ch_name=input("Enter name to check :")
for s in range(length):
    if stud_name[s]==ch_name:
        stud_name[s]="Anamika"
        flag=1
if(flag==0):
    stud_name.insert(1,"Amal")
    
print(stud_name)










