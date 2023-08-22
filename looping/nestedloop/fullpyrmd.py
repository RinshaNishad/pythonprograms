

rows=int(input("enter number of rows:"))
for i in range(5,1,-1):
    for j in range(1,8):
        if(i==2*i-1) or (j==2*j-j):
            print("*",end=" ")
        else:
            print(end=" ")
    print()





