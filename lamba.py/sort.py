lst=[1,56,78,2]

#sort on ascending order
print(sorted(lst))
# or print(sorted(lst,reverse=False))

#sort on descending order
print(sorted(lst,reverse=True))


words=["hello","good","aabbcccdef","morning"]

out=sorted(words,reverse=True,key=lambda w:len(w))
print(out)