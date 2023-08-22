# user=[
#     {"name":"hari","followers":450,"followings":780}
# ]

f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\users\\data.txt","r")

users=[]

for line in f:
    # print(line)
    text=line.rstrip("\n")
    name,followers,followings=text.split(",")
    print(name,followers,followings)
