#sample input 1

arr=[2,3,4]
op=[]
#step1=fin total sum
#step2=sub each element frm total
# total_arr=sum(arr)
for i in arr:
    res=sum(arr)-i
    op.append(res)
    print(res)
print(op)
    # print(total_arr-i)
