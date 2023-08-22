words=["hello","hai","hello","hai","good","morning","evening"]

#word count
#{hello:2,hai:2,good:1,morning:1,evening:1}

# for w in words:
#     print(w)
wc={}
for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
        
print(wc)







