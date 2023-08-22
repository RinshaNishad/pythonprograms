f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\fwrite\\data.txt","w")

# f.write("hi am rinsha")
# print("process file:nishad")

#if w chnge the contnt on f.write() the data file will be rewrtd new content

languages=[
    "python","java","c","c++",".net"
]

for l in languages:
    f.write(l+"\n")
print("finished")
f.close()
