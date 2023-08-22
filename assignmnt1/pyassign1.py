# qn:1

# for i in range(1500,2700):
#     if i%7==0 and i%5==0:
#         print(i)

# ======================================================

# qn2:

# temp_indegree=int(input("enter a value:"))

# fh=(temp_indegree * (9/5)) + 32
# print(f"Value of {temp_indegree} degree in fh :",fh)


# temp_infh=int(input("Enter a value:"))
# degree=(temp_infh -32) *(5/9)
# print(f"Value of {temp_infh} fh in degree :",degree)

# =========================================================

# qn:3

# from re import *
# password=input("enter your password :")
# rule="[a-zA-Z0-9_$#@%&*!]{6,16}"
# matcher=fullmatch(rule,password)
# if matcher:
#     print("it is valid...")
# else:
#     print("not valid...")

# =======================================================

# qn:4

# print("Enter length of the triangle sides: ")
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))

# if x == y == z:
# 	print("Equilateral triangle")
# elif x==y or y==z or z==x:
# 	print("isosceles triangle")
# else:
# 	print("Scalene triangle")

# ========================================================

# qn:5

# user=input("is it raining (yes/no) : ").strip().lower()
# if user=="yes":
#     windy=input("is it windy (yes/no) : ").strip().lower()
#     if windy=="yes":
#         print("It is too windy for an umbrella")
#     else:
#         print("Take an umbrella")
# else:
#     print("Enjoy your day")

# =======================================================

# qn:6

# num=int(input("Enter num 1 or 2:"))


# if num==1:
#     length=int(input("enter length of a side:"))
#     area=length**2
#     print("Area of square is :",area)

# elif num==2:
#     b=int(input("Enter base:"))
#     h=int(input("Enter height:"))
#     triangle_area=(b*h)//2
#     print("Area of triangle is :",triangle_area)

# else:
#     raise Exception("Error found")

# print("1.square")
# print("2.Triangle")
# print("Enter a number")

# =====================================================

# qn:7

# lst=[2,3,4,4,5,5,6,7,1,7,9]

# x = []
# y = []
# for i in lst:
#     if i not in x:
#         x.append(i)
# for i in x:
#     if lst.count(i) > 1:
#         y.append(i)
# print("duplicate elements are :",y)

# =====================================================

# qn:8

# age=int(input("Enter user's age :"))

# if age>=18:
#     print("You can vote..")
# elif age==17:
#     print("You can learn to drive..")
# elif age==16:
#     print("You can buy a lottery ticket..")
# elif age<16:
#     print("You can go for treat..")

# ======================================================

# qn:9

# num=int(input("enter number of people:"))
# if num<10:
#     for i in range(1,num+1):
#         name=input("enter name of person:")
#         print(f"[{name}] has been invited..")
# else:
#     print("Too many people")


# =====================================================

# qn:10

num=int(input("enter number(1,2 or 3):"))
if num==1:
    print("Thank you")
elif num==2:
    print("Well done")
elif num==3:
    print("Correct")
else:
    raise Exception ("Error message")





