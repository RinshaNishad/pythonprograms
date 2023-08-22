# num=9
# for row in range(1, num+1):
    
#     for col in range(0, row):
#         print(" ", end="")

#     for col in range(1, (num*2 - (2*row - 1))+1):

#         if row == 1 or col == 1 or col ==(num*2 -(2*row-1)):
#             print("*", end="")
#         else:
#             print(" ", end="")
    
    # print()

for row in range(1,5):
    for col in range(1,8):
        if(row==4) or (row+col==5) or (col-row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()























