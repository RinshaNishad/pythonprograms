text="hello i am here in kakkanad"
#print longest word

word=text.split(" ")

# print(max(word,key=lambda w:len(w)))


#=========================or==============================

wc={}
for w in word:
    if w not in wc:
        wc[w]=len(w)
print(wc)
print(max(wc))

    