word="fhdflshbfslkhfbskhjildvssdvAAADDDVGFVGFUUNTYNYT08087576442"
wc={}
for w in word:
    if(w in wc):
        wc[w]+=1
    else:
        wc[w]=1
print(wc)