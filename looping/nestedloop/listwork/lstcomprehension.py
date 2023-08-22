#lst comprehension
#syntax: [return value| iteration | condition]


lst=[3,4,5,6,7]

odds=[num for num in lst if num%2!=0]
print("odd lst :",odds)

num_gt_five=[num for num in lst if num>5]
print("number greater than five list :",num_gt_five)

evens=[num for num in lst if num%2==0]
print("even list :",evens)

cubes=[num**3 for num in lst]
print("cubes :",cubes)

squares=[num**2 for num in lst]
print("squares :",squares)

#print all numbers divisible by 3
divisible_3=[num for num in lst if num%3==0]
print("divisible by 3 :",divisible_3)