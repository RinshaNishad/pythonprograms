# lst=[3,4,5,6,7,8,9,10]
# ele=6

# #using linear search method
# #---------------------------
# is_found=False
# for n1 in range(0,len(lst)):
#     if ele==lst[n1]:
#         is_found=True
#         break
# print("found" if is_found==True else "not found")


#using binary search method
#---------------------------
lst=[3,4,5,6,7,8,9,10]
element=11
is_found=False
low=0
upp=len(lst)-1

while(low<=upp):
    mid=(low+upp)//2
    if element==lst[mid]:
        is_found=True
        break
    elif element > lst[mid]:
        low=mid+1
    elif element <lst[mid]:
        upp=mid-1
print("element found" if is_found==True else "element not found")















