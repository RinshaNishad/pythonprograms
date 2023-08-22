num=int(input("Enter num 1 or 2:"))


if num==1:
    length=int(input("enter length of a side:"))
    area=length**2
    print("Area of square is :",area)

elif num==2:
    b=int(input("Enter base:"))
    h=int(input("Enter height:"))
    triangle_area=(b*h)//2
    print("Area of triangle is :",triangle_area)

else:
    raise Exception("Error found")

print("1.square")
print("2.Triangle")
print("Enter a number")

