allusers=["mohanlal","mammootty","fahad","dq","vijay","nivin","asif"]
dq_frndlst=["mohanlal","mammootty","fahad","asif"]
asif_frndlst=["mohanlal","mammootty","fahad","nivin","vijay"]

# suggestions for dq

# suggestns=set(allusers).difference(set(dq_frndlst))
# suggestns.remove("dq")
# print(suggestns)

# dq=>asif  mutual frnds

mutual_frnds=set(dq_frndlst).intersection(set(asif_frndlst))
print(mutual_frnds)
