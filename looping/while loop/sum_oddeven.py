# num=1                          
# odd_sum=0
# even_sum=0
# while num<=20:
#     if num%2!=0:
#         odd_sum+=num
#     else:
#         even_sum+=num
#     num+=1
# print(odd_sum,"is the sum of odd numbers")
# print(even_sum,"is the sum of even numbers")
                  #OR
# start=1
# limit=25                          
# odd_sum=0
# even_sum=0
# while start<=limit:
#     if start%2!=0:
#         odd_sum+=start
#     else:
#         even_sum+=start
#     start+=1
# print(odd_sum,"is the sum of odd numbers")
# print(even_sum,"is the sum of even numbers")


#using for loop

start=1
limit=25

odd_sum=0
even_sum=0
for num in range(start,limit):
    if num%2==0:
        even_sum+=num
    else:
        odd_sum+=num
print("odd sum",odd_sum)
print("even sum",even_sum)

