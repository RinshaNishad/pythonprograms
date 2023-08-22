lst=[2,3,4,5,6,7,8]
ele=int(input("Enter an element to serach :"))
is_found=False
low=0
upp=len(lst)-1
while(low<=upp):
    mid=(low+upp)//2
    if ele==lst[mid]:
        is_found=True
        break
    elif ele>lst[mid]:
        low=mid+1
    elif ele<lst[mid]:
        upp=mid-1
print("found" if is_found==True else "not found")