#select a range of 10 no:s,check whether the no. is divisible
#by 9,if divisible by 9,then the result shoulb be printed as
#(number*9) 


# for i in range(20,30):
#     if(i%9==0):
#         print(f"{i} * 9 = {i*9}")

fst=int(input("enter below range :"))
scnd=int(input("enter above range :"))

for i in range(fst,scnd):
    if i%9==0:
        print(f"{i} * 9 = {i*9}")