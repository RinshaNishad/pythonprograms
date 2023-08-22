text="ABBAACDA"

#==> most recursive char
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(max(wc,key=lambda key:wc.get(key)))

