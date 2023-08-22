#==>
movies={"2018":5,"keralastory":3,"neymar":4,"kgf":5,"arm":4}

#==> print all movie names

print(movies.keys())


#==> print top rated movie

print(max(movies,key=lambda key:movies.get(key)))

#==>sort movies with respect to rating by descending order

print(sorted(movies,reverse=True,key=lambda key:movies.get(key)))