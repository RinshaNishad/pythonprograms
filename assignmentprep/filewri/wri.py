f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\assignmentprep\\filewri\\data.txt","w") 

movies=[
    "cid moosa","916","july 14","2018"
    ]
for m in movies:
    f.write(m+"\n")
print("finish")
f.close()
    

