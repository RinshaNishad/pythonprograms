word="observe"         #input("enter a word :")
out="see"   #input("enter another word :")
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
      break
print(is_kangaroo)







           