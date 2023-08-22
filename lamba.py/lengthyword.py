words=["hello","good","aabbcccdef","morning"]

print(max(words,key=lambda w:len(w)))

print(min(words,key=lambda w:len(w)))

