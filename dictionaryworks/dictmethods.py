students={"roll":123,"name":"nyha","age":25,"course":"mca"}
#==> values() method return all values in dictionary

# print(students.values())

#==>keys() method return all keys in dictionary
# print(students.keys())

#==> items() will return both keys and values
# print(students.items())

# for k,v in students.items():
#     print(k,v)

#==> pop(key) to remove a key
students.pop("course")
print(students)

#==> get(key) fetching value with key

# print(students.get("name")) # or print(students["name"])

#==>diff btw using [] and get() method for fetchng value
#when using [] if key name is invalid,the prgm will stop and balnc code 
# will not wrk..bt if we use get() method if the key is invalid "none" 
# value is returnd nd blnc prgm will execute....

# eg:
# print(students["names"])
# print(students.get("names"))
# print("file transfer")
# print("database commit")








