lst=[5,3,4,2]

sum=int(input("Enter a digit:"))
low=0
upp=len(lst)-1


while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if(cur_sum==sum):
        print("pairs :",lst[low],lst[upp])
        break
    elif(cur_sum<sum):
        low+=1
    elif(cur_sum>sum):
        upp-=1
        