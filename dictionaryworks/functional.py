lst=[1,2,3,4,5]

#print squares of all numbers
#using map()=======================================
def square(num):
    return num**2
square=list(map(square,lst))
print(square)
#=======================or by using lambda==============================

squares=list(map(lambda n:n**2,lst))
print(squares)

# list_squares=[n**2 for n in lst]
# print(list_squares)
#===================================================
cubes=list(map(lambda n:n**3,lst))
print(cubes)
# list_cubes=[n**3 for n in lst]
# print(list_cubes)

#=================================================
#using filter()=========================
odds=list(filter(lambda n:n%2!=0,lst))
print(odds)
# list_odds=[n for n in lst if n%2!=0]
# print(list_odds)

evens=list(filter(lambda n:n%2==0,lst))
print(evens)
# list_evens=[n for n in lst if n%2==0]
# print(list_evens)


num_gt3=list(filter(lambda n:n>3,lst))
print(num_gt3)
# list_gt3=[n for n in lst if n>3]
# print(list_gt3)

#==============================================================
