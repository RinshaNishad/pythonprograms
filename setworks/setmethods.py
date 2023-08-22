# print(dir(list))---print all methods in list
#-----------------------------------------------

# st={1,2,3,4,5,6}
# st.add(100)
# st.add("hello")
# st.add("True")
# st.add(100.1)
# print(st)
#-------------------------------------------------

#==> Convert list into set

# lst=[1,2,3,4,5,6,7]
# st=set(lst)
# print(st)

#-------------------------------------------------

#==> Union,Intersection,Difference

st1={10,11,12,13}
st2={10,12,25,30}

union_set=st1.union(st2)
print(union_set)

intersectn_set=st1.intersection(st2)
print(intersectn_set)

diff_set=st1.difference(st2)
print(diff_set)

diff_set2=st2.difference(st1)
print(diff_set2)

# set_update=st1.update(st2)
# print(st1)

set_updt=st2.update(st1)
print(st2)
print(st1)












