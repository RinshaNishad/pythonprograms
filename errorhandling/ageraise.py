age=int(input("enter age:"))

# raise----used to create custom error

if age<18:
    raise Exception("invalid age")

else:
    print("valid")