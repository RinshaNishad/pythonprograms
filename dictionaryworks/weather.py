weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22},

]

#{"tvm":26,"apy":23,"kty":28,...}

temp={}
for t in weather:
    for k,v in t.items():
        dist_name=k
        curnt_weathr=v
        if dist_name in temp:
            old_temp=temp[dist_name]
            if curnt_weathr>old_temp:
                temp[dist_name]=curnt_weathr
        else:
            temp[dist_name]=curnt_weathr
print(temp)
print(max(temp,key=lambda key:temp.get(key)))





