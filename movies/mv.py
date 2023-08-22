from json import load

with open("C:\\Users\\DELL\\Desktop\\pythonworks\\movies\\mdb.json","r",encoding="UTF-8") as f:
    data=load(f)

#==> print total no of movies

# print(len(data))

#==================================================================

#==> print all movie names

# movie_names=[d.get("title") for d in data]
# print(movie_names)

#==============================================================

#==> print movie with hightst runtime

# high_runtime=max(data,key=lambda m:int(m.get("runtime")))
# print(high_runtime.get("title"))

#=====================================================================

#==> print all genres

# all_genres={g for m in data for g in m.get("genres")}
# print(all_genres)

#===============================================================

#==> print movie name which contain genre comedy

# comedy_movie=[m.get("title") for m in data if "Comedy" in m.get("genres")]
# print(comedy_movie)

#===================================================================
#==> print movie name which contain genre comedy or fantasy

# comedy_fantasy=[m.get("title") for m in data if "Comedy" or "Fantasy" in m.get("genres")]
         #=====================or================================
# comedy_fantasy={m.get("title") for m in data for g in m.get("genres") if g in ["Comedy","Fantasy"]}
# print(comedy_fantasy)
#==> yearwise movie count {1988:?,1987:?,......}

yc={}
for m in data:
    year=m.get("year")
    if year in yc:
        yc[year]+=1
    else:
        yc[year]=1
# print(yc)
print(max(yc,key=lambda k:yc.get(k)))
print(min(yc,key=lambda k:yc.get(k)))



