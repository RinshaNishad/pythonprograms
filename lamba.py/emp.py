employee={"id":100,"name":"manu","department":"hr","salary":40000}

#==> create a function for returning employee name

# def get_name(emp):
#     return emp.get("name")
# print(get_name(employee))

# get_name=lambda emp:emp.get("name")
# print(get_name(employee))

#==> create a lambda functn for returning salary

# get_salary=lambda emp:emp.get("salary")
# print(get_salary(employee))


#==> *args positional argument takes any numbr of parameters..type-tuple

# def addition(*args):
#     return sum(args)

# addition=lambda *args:sum(args)

# print(addition(10,20))
# print(addition(10,20,30))

max_nums=lambda *args:max(args)
print(max_nums(10,2,3,4,50))








