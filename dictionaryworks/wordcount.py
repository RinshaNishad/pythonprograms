text="ABABC"

#==> find first recursive character

# wc={}
# for ch in text:
#     if(ch in wc):
#         print(ch,"is first recursive character")
#         break  #----if we avoid break it'll prnt all recrsv char in txt
#     else:
#         wc[ch]=1


#==> find count of all characters
wc={}
for ch in text:
    if ch in wc:
        # wc[ch] # or
        wc[ch]+=1
    else:
        wc[ch]=1
        # print(ch,"is",text.count(ch)," in times")
print(wc)