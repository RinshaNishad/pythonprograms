# qn1

# emplst=[]
# for i in range(3):
#     name=input("Enter three names:")
#     emplst.append(name)
# print(emplst)

# qn=input("Do u wantt to add another (yes/no):").strip().lower()
# while qn=="yes":
#     qn=input("Do u wantt to add another (yes/no):").strip().lower()
#     if qn=="yes":
#         name=input("Enter names:")
#         emplst.append(name)
#     else:
#        break
# print(f"Total no. of people invited to party is {len(emplst)}")

# ================================================================================================

# qn2

# print("The guests are:",emplst)
# g_name=input("Enter name from list:")
# if g_name in emplst:
#     postn=emplst.index(g_name)
# print(f"The position of {g_name} is {postn}")

# is_attend=input("Do u want to attend the party (yes/no):").strip().lower()
# if is_attend=="no":
#     emplst.remove(g_name)
# print("Updated list is :",emplst)

# =================================================================================================

# qn3

# lst=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

# row=int(input("Enter row to display:"))
# print(lst[row-1])
# value=int(input("Enter new value to add:"))
# lst[row-1].append(value)
# print("Updated row is :",lst[row-1])

# =====================================================================================================

# qn4

# user=[]
# for i in range(4):
#     name=input("Enter name:")
#     age=int(input("Enter age:"))
#     id=int(input("Enter id :"))
#     user.append({"name":name,"age":age,"id":id})
# print(user)
# search=input("Enter name frm list:")
# for u in user:
#     if u.get("name")==search:
#         print("Age is :",u.get("age"))
#         print("id is :",u.get("id"))

# ==================================================================================================================

# qn5

# user=[]
# for i in range(4):
#     name=input("Enter name:")
#     age=int(input("Enter age:"))
#     id=int(input("Enter id :"))
#     user.append({"name":name,"age":age,"id":id})
# print(user)
# for u in user:
#     print(u.get("name"),u.get("id"))


# =============================================================================================================

# qn6

library=[
    {"title":"Aadujeevitham","author":"Benyamin","year":2008 ,"genre":["Novel","fiction"]},
    {"title":"Pride and prejudice","author":"Jane Austen","year":1813 ,"genre":["Classic Regency novel","Romance novel"]},
    {"title":"Randamoozham","author":"M.T.Vasudevan Nair","year":2008 ,"genre":["Mythology","drama","historical fiction"]},
    {"title":"Oliver Twist","author":"Charles Dickens","year":1838 ,"genre":["Serial novel"]},
    {"title":"Aarachar","author":"K.R.Meera","year":2012 ,"genre":["Novel"]},
    {"title":"Romeo and Juliet","author":"William Shakespeare","year":1597 ,"genre":["Tragedy"]}
    
]

# update author
# for l in library:
#     if l.get("title")=="Aarachar":
#         l["author"]="Meera"
# print(library)

# =======================================================

# year_filter=[l.get("title") for l in library if l.get("year")<=2000]
# print(len(year_filter))
# ========================================================
# add new item
# new_item={"title":"Half Girlfriend","author":"Chetan Bhagat","year":2014,"genre":["Fiction","Comedy"]}
# library.append(new_item)
# print(library)



