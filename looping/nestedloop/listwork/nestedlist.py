#nested list

lst=[
    [1,2],
    [4,50],
    [50,45],
]

#print all numbers in nested  list

# for ls in lst:
#     for num in ls:
#         print(num)

allnumbers=[num for ls in lst for num in ls]
print(allnumbers)

#print all numbers >5

# for ls in lst:
#     for num in ls:
#         if(num > 5):
            # print(num)

num_gt_five=[num for ls in lst for num in ls if num>5]
print(num_gt_five)
        
       
        