movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"tamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"tamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}

]

#==>print all movie names
for m in movies:
    print(m.get("name"))
#list comprehensn:=======or=============
movie_names=[m.get("name") for m in movies]
print(movie_names)
#===============================end================================

# print filter movies with genre=mystery
for m in movies:
    if "mystery" in m.get("genres"):
        print(m.get("name"))
    #=============or==================
m_name=[m.get("name") for m in movies if "mystery" in m.get("genres")]
print(m_name)
#=================================end===============================

# top rated movie names

print(max(movies,key=lambda m:m.get("rating")))
#============================end===================================
# print malayalam movie names
for m in movies:
    if "malayalam" in m.get("language"):
        print(m.get("name"))
#=========================end=====================================
# movie names released in 2023
for m in movies:
    if m.get("year")==2023:
        print(m.get("name"))
    #=======================or=====================
year_filter=[m.get("name") for m in movies if m.get("year")==2023]
print(year_filter)
#==========================end====================================
# sort movies wrt rating in desc order
print(sorted(movies,reverse=True,key=lambda m:m.get("rating")))