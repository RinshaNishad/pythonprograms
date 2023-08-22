data={
    "django":"framework",
    "react":"library",
    "fastapi":"framework",
    "vue":"framework",
    "ajax":"library"
    }
# o/p={"framework":4,"library":2}
# wc={}
# for v  in data.values():
#     if v in wc:
#         wc[v]+=1
#     else:
#         wc[v]=1
# print(wc)

# o/p={"framework":["django","fastapi","vue"],"library":["ajax","react"]}

wc={}
for k,v in data.items():
    if v in wc:
        wc[v].append(k)
    else:
        wc[v]=[k]
print(wc)
