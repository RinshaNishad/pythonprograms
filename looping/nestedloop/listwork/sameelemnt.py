lst1=[10,14,15,20,21]
lst2=[8,9,20,21,22]
(p1,p2)=(0,0)
while(p1<len(lst1) and p2<len(lst2)):
    if(lst1[p1]==lst2[p2]):
        print("common element",lst1[p1])
        p1+=1
        
    elif(lst1[p1]< lst2[p2]):
        p1+=1
    elif(lst1[p1]>lst2[p2]):
        p2+=1








# # count=1

# for n1 in lst1:
#     for n2 in lst2:
#         if(n1==n2):
#             print(n1)
#             break
# #         count+=1
# # print("iteration",count)
        
