from json import load

with open("C:\\Users\\DELL\\Desktop\\pythonworks\\jsonproces\\data.json","r") as f:
    data=load(f)

# print(data)
# names=[u.get("name") for u in data]
# print(names)

# student with highest total

# student=max(data,key=lambda u:u.get("total"))
# print(student)

#sort all stud wrt total by desc order

out=sorted(data,reverse=True,key=lambda s:s.get("total"))
print(out)

# print bca stud names

bca_stud=[u.get("name") for u in data if u.get("course")==("bca")]
print(bca_stud)