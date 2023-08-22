#find duplicate element frm lst

lst=[2,3,4,4,5,5,6,7]
# new=[]
# for i in lst:
#     num=lst.count(i)
#     if num > 1:
#         if new.count(i)==0:
#             new.append(i)
# print(new)
#---------------------------------------------------
x = []
y = []
for i in lst:
    if i not in x:
        x.append(i)
for i in x:
    if lst.count(i) > 1:
        y.append(i)
print(y)








# p1=0
# p2=len(lst)-1
# for p1 in len[lst]:
#     for p2 in len[lst]-1:
#         if p1==p2:
#             print("dup",p1)
#             break
#         elif p1<p2:
#             p1+=1
#         elif p1>p2:
#             p2-=1
