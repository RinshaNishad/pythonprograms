# f=open("C:/Users/DELL/Desktop/pythonworks/fileinputoutput/data.txt","r")
# for line in f:
#     print(line)
#===============================or=====================================
#==>print all words in string

# f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\fileinputoutput\\data.txt","r")
# words=[]
# for line in f:
#     # line=line.rstrip("\n")
#     # text=line.split(" ")
#     text=line.rstrip("\n").split(" ")
#     for w in text:
#         # if w in words:
#         words.append(w)
# print(words)

#======================================================================
#==> print unique elements in string

# f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\fileinputoutput\\data.txt","r")
# words=[]
# for line in f:
#     # line=line.rstrip("\n")
#     # text=line.split(" ")
#     text=line.rstrip("\n").split(" ")
#     for w in text:
#         if w not in words:
#             words.append(w)
# print(words)
# f.close()

#=================================or======================================
f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\fileinputoutput\\data.txt","r")
words=set()
for line in f:
    # line=line.rstrip("\n")
    # text=line.split(" ")
    text=line.rstrip("\n").split(" ")
    for w in text:
        
        words.add(w)
print(words)
f.close()