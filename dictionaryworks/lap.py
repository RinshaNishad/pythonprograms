lap={"id":100,"name":"Dell","price":60000}
print(lap["id"])
if ("price" in lap):
    print(lap["price"])

#==> print all key value pair

for key in lap:
    print(key,":",lap[key])

#==> add new key value pair
lap["processor"]="intel core i5"
print(lap)

#==> add 500 rs discount
lap["price"]-=500
print(lap)

