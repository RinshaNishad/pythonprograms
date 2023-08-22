#{key:value,key:value,.........,key:value}


emp={"id":100,"name":"Nyha","desig":"HR","salary":40000}
# print(emp)

# #==> print emp name,salary,designtn
# print(emp["name"])
# print(emp["salary"])
# print(emp["desig"])

#==>  iteration

for key in emp:
    print(key,":",emp[key])

#==> adding new key-value pair-----dictname["key"]=value
emp["gender"]=["female"]
print(emp)

#==> updating a value-----dictname["key"]=new value
emp["salary"]=45000
print(emp["salary"])

#==> update emp salary with current salary +2000
emp["salary"]+=2000
print(emp["salary"])

#==> check existence of a key

if("name" in emp):
    print("present")
else:
    print("not present")


