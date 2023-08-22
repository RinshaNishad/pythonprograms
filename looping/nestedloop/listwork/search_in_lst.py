#membership operators in python=>in...not in

lst=[12,13,15,20,16]
# if 15 in lst:
#     print("15 is present")
# else:
#     print("15 is not present")

# if 21 not in lst:
#     print("21 is not present")
# else:
#     print("21 is present")

# cars=["maruthi","swift","cheverlet","benz","bmw","lamborgini"]
# car_i=[]
# for c in cars:
#     if "i" in c:
#         car_i.append(c)
# print(car_i)


#remove 1st,3rd and 4th element frm the lst
# lst=[2,5,7,10,15]
# lst.pop(0)
# print(lst)
# lst.pop(2-1)
# print(lst)
# lst.pop(3-2)
# print(lst)



#create a new list from a given list of integers
#of the new list should be odd and multiples of 5

"""
lst=[1,5,13,15,20,21,25,38]
new_lst=[]
for num in lst:
    if num%2!=0 and num%5==0:
        new_lst.append(num)
print(new_lst)

"""


#find greatest value frm a given lst without using max() function.

"""
lst=[2,6,10,15,5]
maxim=lst[0]
for l in lst:
    if maxim<l:
        maxim=l
print("maximum value in list :",maxim)

"""

#find minimum value frm a given lst without using min() fn. and remove frm lst.

lst=[2,6,10,15,5]
minim=lst[0]
for l in lst:
    if minim>l:
        minim=l
print("minimum value in list :",minim)
lst.remove(minim)
print("list aftr removing minimum value :",lst)






