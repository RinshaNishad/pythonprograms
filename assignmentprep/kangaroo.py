word="observe"
out="seebs"

wc={}
is_kangaroo=True
for w in word:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1

for ch in out:
    if ch in wc and wc[ch]>0:
        wc[ch]-=1
    else:
        is_kangaroo=False
print("kangaroo" if is_kangaroo==True else "not kangaroo")