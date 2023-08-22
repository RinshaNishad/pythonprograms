car={"name":"swift","brand":"nexa","fueltype":"petrol","rate":300000}


print(car["name"])

if "price" in car:
    print(car["price"])
else:
    print("price not updated")

for key in car:
    print(key,":",car[key])

car["rate"]-=500
print(car)






# c={}
# for key in car:
#     if key in c:
#         c[key]+=1
#     else:
#         c[key]=1
# print(c)












